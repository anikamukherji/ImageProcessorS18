import pymodm
from pymodm import connect
from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime
from skimage import exposure
import base64
import numpy as np
import uuid
import os
import math
from skimage import util
import PIL
from user import create_user, already_user, add_uploadimage, add_image_hist
from user import add_image_contrast, add_image_log, add_image_reverse
from models import User
import logging
import models
from Server.image_module.decode_image import *
from Server.image_module.encode_image import *
from Server.image_module.histogram_equalization import *
from Server.image_module.image_histogram import *
from Server.image_module.log_compression import *
from Server.image_module.reverse_video import *
from Server.image_module.contrast_stretching import *
from Server.image_module.strip_image import *
from PIL import Image

app = Flask(__name__)
CORS(app)
connect("mongodb://localhost:27017/image_app")


@app.route("/api/user_exists/<username>", methods=["GET"])
def user_exists(username):
    """
    Returns whether username is already taken
    :return: json dict of new user initial info
    :rtype: Request
    :return: 4xx error with json error dict if missing key
             or incorrect type given
    """
    user_exists = already_user(username)
    return jsonify(user_exists), 200


@app.route("/api/new_user", methods=["POST"])
def post_new_user():
    """
    Posts new user
    :return: json dict of new user initial info
    :rtype: Request
    :return: 4xx error with json error dict if missing key
             or incorrect type given
    """
    r = request.get_json()
    try:
        username = r["username"]
    except KeyError as e:
        logging.warning("Incorrect JSON input:{}".format(e))
        err = {"error": "Incorrect JSON input"}
        return jsonify(err), 400
    if already_user(username):
        u_vals = {"warning": "This user_name is already existed"}
    else:
        u_vals = create_user(username)
    return jsonify(u_vals), 200


@app.route("/api/upload", methods=["POST"])
def image_post():
    """
    Posts new user with given image
    :return: json dict of new user values
    :rtype: Request
    :return: 4xx error with json error dict if missing key
             or incorrect type given
    :rtype: Request
    """
    r = request.get_json()
    try:
        username = r["username"]
        image_new = r["image"]
        assert type(image_new) is str
    except KeyError as e:
        logging.warning("Incorrect JSON input:{}".format(e))
        err = {"error": "Incorrect JSON input"}
        return jsonify(err), 400
    except AssertionError as e:
        logging.warning("Incorrect image type given: {}".format(e))
        err = {"error": "Incorrect image type given"}
        return jsonify(err), 400
    if already_user(username):
        u_vals = add_uploadimage(username, image_new, datetime.datetime.now())
    else:
        u_vals = create_user(username)
        u_vals = add_uploadimage(username, image_new, datetime.datetime.now())
    logging.debug("adding new image to user: {}".format(u_vals))
    return jsonify(u_vals), 200


@app.route("/api/<username>", methods=["GET"])
def get_user(username):
    """
    Get the user with the whole info
    :return: json dict of user values
    :rtype: Request
    """
    if already_user(username):
        user = models.User.objects.raw({"_id": username}).first()
        u_values = {"user_name": user.username,
                    "upload_image": user.image_original,
                    "upload_time": user.upload_time
                    }
        return jsonify(u_values), 200
    else:
        u_values = {"warning": "This user does not exist"}
        return jsonify(u_values), 200


@app.route("/api/histogram_equalization", methods=["POST"])
def histogram_equalization_processing():
    """
    Get the processed image with histogram
    :return: json dict of image
    :rtype: Request
    """
    r = request.get_json()
    try:
        username = r["username"]
        image = r["image"]
        file_type = r["file_type"]
        assert type(image) == str
    except KeyError as e:
        logging.warning("Incorrect JSON input: {}".format(e))
        err = {"error": "Incorrect JSON input"}
        return jsonify(err), 400
    except AssertionError as e:
        logging.warning("Incorrect image type given: {}".format(e))
        err = {"error": "Incorrect image type given"}
        return jsonify(err), 400
    stripped_image = strip_image(image, file_type)

    suffix = "." + file_type
    suffix_id2 = ".png"
    # id1 is where the original file will be stored
    filename1 = str(uuid.uuid4())
    id1_temp = filename1 + suffix
    # id2 is where the processed file will be stored
    filename2 = str(uuid.uuid4())
    id2 = filename2 + suffix_id2

    start_time = datetime.datetime.now()
    decode_image(stripped_image, id1_temp)
    id1 = filename1 + ".png"
    im = Image.open(id1_temp)
    im.save(id1)
    # processed_image dictionary will be returned
    processed_image = histogram_equalization(id1, id2)
    # histogram_original = histogram(id1)
    # histogram_processed = histogram(id2)
    end_time = datetime.datetime.now()
    process_time = str(end_time - start_time)

    if username != 'Visitor':
        num_hist = add_image_hist(username, id2, datetime.datetime.now())
        processed_image["process_count"] = num_hist

    # processed_image["histogram_original"] = histogram_original
    # processed_image["histogram_processed"] = histogram_processed
    processed_image["process_time"] = process_time

    print("returning processed image")
    return jsonify(processed_image), 200


@app.route("/api/contrast_stretching", methods=["POST"])
def contrast_stretching_processing():
    """
    Get the processed image with contrast-stretching
    :param id1: uuid of original image
    :param id2: uuid of processed image
    :return: json dict of image
    :rtype: Request
    """
    r = request.get_json()
    try:
        username = r["username"]
        image_new = r["image"]
        file_type = r["file_type"]
        assert type(image_new) is str
    except KeyError as e:
        logging.warning("Incorrect JSON input: {}".format(e))
        err = {"error": "Incorrect JSON input"}
        return jsonify(err), 400
    except AssertionError as e:
        logging.warning("Incorrect image type given: {}".format(e))
        err = {"error": "Incorrect image type given"}
        return jsonify(err), 400
    stripped_string = strip_image(image_new, file_type)

    id1 = str(uuid.uuid4())
    suffix = ".png"
    id1 = id1 + suffix
    id2 = str(uuid.uuid4())
    id2 = id2 + suffix

    start_time = datetime.datetime.now()
    decode_image(stripped_string, id1)
    processed_image = contrast_stretching(id1, id2)
    # histogram_original = histogram(id1)
    # histogram_processed = histogram(id2)
    end_time = datetime.datetime.now()
    process_time = str(end_time - start_time)

    if username != 'Visitor':
        num_contrast = add_image_contrast(username,
                                          id2, datetime.datetime.now())
        processed_image["process_count"] = num_contrast

    # processed_image["histogram_original"] = histogram_original
    # processed_image["histogram_processed"] = histogram_processed
    processed_image["process_time"] = process_time
    return jsonify(processed_image), 200


@app.route("/api/log_compression", methods=["POST"])
def log_compression_processing():
    """
    Get the processed image with log_compression
    :param id1: uuid of original image
    :param id2: uuid of processed image
    :return: json dict of image
    :rtype: Request
    """
    r = request.get_json()
    try:
        username = r["username"]
        image_new = r["image"]
        file_type = r["file_type"]
        assert type(image_new) is str
    except KeyError as e:
        logging.warning("Incorrect JSON input: {}".format(e))
        err = {"error": "Incorrect JSON input"}
        return jsonify(err), 400
    except AssertionError as e:
        logging.warning("Incorrect image type given: {}".format(e))
        err = {"error": "Incorrect image type given"}
        return jsonify(err), 400
    stripped_string = strip_image(image_new, file_type)

    id1 = str(uuid.uuid4())
    suffix = ".png"
    id1 = id1 + suffix
    id2 = str(uuid.uuid4())
    id2 = id2 + suffix

    start_time = datetime.datetime.now()
    decode_image(stripped_string, id1)
    processed_image = log_compression(id1, id2)
    end_time = datetime.datetime.now()
    # histogram_original = histogram(id1)
    # histogram_processed = histogram(id2)
    end_time = datetime.datetime.now()

    process_time = str(end_time - start_time)

    if username != 'Visitor':
        num_log = add_image_log(username, id2, datetime.datetime.now())
        processed_image["process_count"] = num_log

    # processed_image["histogram_original"] = histogram_original
    # processed_image["histogram_processed"] = histogram_processed
    processed_image["process_time"] = process_time
    return jsonify(processed_image), 200


@app.route("/api/reverse_video", methods=["POST"])
def reverse_video_processing():
    """
    Get the processed image with reverse_video
    :param id1: uuid of original image
    :param id2: uuid of processed image
    :return: json dict of image
    :rtype: Request
    """
    r = request.get_json()
    try:
        username = r["username"]
        image_new = r["image"]
        file_type = r["file_type"]
        assert type(image_new) is str
    except KeyError as e:
        logging.warning("Incorrect JSON input: {}".format(e))
        err = {"error": "Incorrect JSON input"}
        return jsonify(err), 400
    except AssertionError as e:
        logging.warning("Incorrect image type given: {}".format(e))
        err = {"error": "Incorrect image type given"}
        return jsonify(err), 400
    stripped_string = strip_image(image_new, file_type)

    id1 = str(uuid.uuid4())
    suffix = ".png"
    id1 = id1 + suffix
    id2 = str(uuid.uuid4())
    id2 = id2 + suffix

    start_time = datetime.datetime.now()
    decode_image(stripped_string, id1)
    processed_image = reverse_video(id1, id2)
    # histogram_original = histogram(id1)
    # histogram_processed = histogram(id2)
    end_time = datetime.datetime.now()
    process_time = str(end_time - start_time)

    if username != 'Visitor':
        num_reverse = add_image_reverse(username, id2, datetime.datetime.now())
        processed_image["process_count"] = num_reverse

    # processed_image["histogram_original"] = histogram_original
    # processed_image["histogram_processed"] = histogram_processed
    processed_image["process_time"] = process_time
    return jsonify(processed_image), 200


if __name__ == "__main__":
    app.run()
