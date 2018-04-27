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
import  PIL
from user import create_user,already_user, add_uploadimage, add_image_hist, add_image_contrast, add_image_log, add_image_reverse
from models import User
import logging
import models

app = Flask(__name__)
CORS(app)
connect("mongodb://vcm-3551.vm.duke.edu:27017/image-app")  # open up connection to db  ????

@app.route("/api/new_user",methods=["POST"])
def user_post():
	"""
	Posts new user

	:return: json dict of new user initial info
	:rtype: Request
	:return: 4xx error with json error dict if missing key
		 or incorrect type given
	"""
	r = request.get_json()
	try:
                email = r["user_email"]
	except KeyError as e:
                logging.warning("Incorrect JSON input:{}".format(e))
                err = {"error": "Incorrect JSON input"}
                return jsonify(err),400
	if already_user(email):
		u_vals = {"warning":"This user_name is already existed"}
	else:
		u_vals = create_user(email)
	return jsonify(u_vals),200
	
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
		email = r["user_email"]
		image_new = r["image"]
		assert type(image_new) is str
	except KeyError as e:
		logging.warning("Incorrect JSON input:{}".format(e))
		err = {"error": "Incorrect JSON input"}
		return jsonify(err),400
	except AssertionError as e:
		logging.warning("Incorrect image type given: {}".format(e))
		err = {"error": "Incorrect image type given"}
		return jsonify(err), 400
	if already_user(email):
		u_vals = add_uploadimage(email,image_new, datetime.datetime.now())
	else:
		u_vals = create_user(email)
		u_vals = add_uploadimage(email, image_new, datetime.datetime.now())
	logging.debug("adding new image to user: {}".format(u_vals))
	return jsonify(u_vals),200

@app.route("/api/<user_email>", methods=["GET"])
def get_image(user_email):
	"""
	Get the user with the whole info

	:return: json dict of user values
	:rtype: Request
	"""
	if already_user(user_email):
		user = models.User.objects.raw({"_id": user_email}).first()
		u_values = {"user_name": user.email,
		    	    "upload_image": user.image_original,
		    	    "upload_time": user.upload_time
		   	   }	
		return jsonify(u_values),200
	else:
		u_values ={"warning": "This user does not exist"}
		return jsonify(u_values),200


@app.route("/api/histogram", methods=["POST"])
def histogram_processed():
	"""
	Get the processed image with histogram

	:return: json dict of image
	:rtype: Request
	"""
	r = request.get_json()
	try:
		email = r["user_email"]
		image_new = r["image"]
		assert type(image_new) is str
	except KeyError as e:
		logging.warning("Incorrect JSON input: {}".format(e))
		err = {"error": "Incorrect JSON input"}
		return jsonify(err),400
	except AsserionError as e:
		logging.warning("Incorrect image type given: {}".format(e))
		err = {"error": "Incorrect image type given"}
		return jsonify(err),400 
	string_to_use = strip_image(image_new)
	id1 = str(uuid.uuid4())
	suffix = ".png"
	id1 = id1 + suffix
	id2 = str(uuid.uuid4())
	id2 = id2 + suffix 
	start_time = datetime.datetime.now()
	decode_image_string(image_new, id1)
	processed_image = histogram_equalization(id1,id2)
	#processed_image = {"1": "asdfer123","2": "123"}
	histogram_ori = histogram(id1)
	#histogram_ori = "yz123"
	histogram_pro = histogram(id2)
	#histogram_pro = "yz398"
	end_time = datetime.datetime.now()
	#id2 = "123456"
	processed_time = str(end_time-start_time)
	num_hist = add_image_hist(email,id2,datetime.datetime.now())
	processed_image["histogram_original"] = histogram_ori
	processed_image["histogram_processed"] = histogram_pro
	processed_image["processed_time"] = processed_time
	processed_image["histogram_equation_times"] = num_hist
	return jsonify(processed_image),200

@app.route("/api/contrast", methods=["POST"])
def contrast_processed():
	"""
        Get the processed image with contrast-stretching
	:param id1: uuid of original image
	:param id2: uuid of processed image
        :return: json dict of image
        :rtype: Request
	"""
	r = request.get_json()
	try:
		email = r["user_email"]
		image_new = r["image"]
		assert type(image_new) is str
	except KeyError as e:
		logging.warning("Incorrect JSON input: {}".format(e))
		err = {"error": "Incorrect JSON input"}
		return jsonify(err),400
	except AsserionError as e:
		logging.warning("Incorrect image type given: {}".format(e))
		err = {"error": "Incorrect image type given"}
		return jsonify(err),400
	string_to_use = strip_image(image_new)
	id1 = str(uuid.uuid4())
	suffix = ".png"
	id1 = id1 + suffix
	id2 = str(uuid.uuid4())
	id2 = id2 + suffix
	start_time = datetime.datetime.now()
	decode_image_string(image_new, id1)
	processed_image = contrast_stretching(id1, id2)
	histogram_ori = histogram(id1)
	histogram_pro = histogram(id2)
	end_time = datetime.datetime.now()
	processed_time = str(end_time - start_time)
	num_contrast = add_image_contrast(email,id2,datetime.datetime.now())
	processed_image["histogram_original"] = histogram_ori
	processed_image["histogram_processed"] = histogram_pro
	processed_image["processed_time"] = processed_time
	processed_image["contrast_streching_times"] = num_contrast
	return jsonify(processed_image),200

@app.route("/api/log", methods=["POST"])
def log_processed():
	"""
        Get the processed image with log_compression
	
	:param id1: uuid of original image
	:param id2: uuid of processed image
        :return: json dict of image
        :rtype: Request
 	"""
	r = request.get_json()
	try:
		email = r["user_email"]
		image_new = r["image"]
		assert type(image_new) is str
	except KeyError as e:
		logging.warning("Incorrect JSON input: {}".format(e))
		err = {"error": "Incorrect JSON input"}
		return jsonify(err),400
	except AsserionError as e:
		logging.warning("Incorrect image type given: {}".format(e))
		err = {"error": "Incorrect image type given"}
		return jsonify(err),400
	string_to_use = strip_image(image_new)
	id1 = str(uuid.uuid4())
	suffix = ".png"
	id1 = id1 + suffix
	id2 = str(uuid.uuid4())
	id2 = id2 + suffix
	start_time = datetime.datetime.now()
	decode_image_string(image_new, id1)
	processed_iamge = log_compression(id1, id2)
	end_time = datetime.datetime.now()
	histogram_ori = histogram(id1)
	histogram_pro = histogram(id2)
	end_time = datetime.datetime.now()
	processed_time = str(end_time-start_time)
	num_log = add_image_log(email,id2,datetime.datetime.now())
	processed_image["histogram_original"] = histogram_ori
	processed_image["histogram_processed"] = histogram_pro
	processed_image["processed_time"] = processed_time
	processed_image["log_compression_times"] = num_log
	return jsonify(processed_image)

@app.route("/api/reverse", methods=["POST"])
def reverse_processed():
	"""
        Get the processed image with reverse_video

	:param id1: uuid of original image
	:param id2: uuid of processed image
        :return: json dict of image
        :rtype: Request
	"""
	r = request.get_json()
	try:
		email = r["user_email"]
		image_new = r["image"]
		assert type(image_new) is str
	except KeyError as e:
		logging.warning("Incorrect JSON input: {}".format(e))
		err = {"error": "Incorrect JSON input"}
		return jsonify(err),400
	except AsserionError as e:
		logging.warning("Incorrect image type given: {}".format(e))
		err = {"error": "Incorrect image type given"}
		return jsonify(err),400
	string_to_use = strip_image(image_new)
	id1 = str(uuid.uuid4())
	suffix = ".png"
	id1 = id1 + suffix
	id2 = str(uuid.uuid4())
	id2 = id2 + suffix
	start_time = datetime.datetime.now()
	decode_image_string(image_new, id1)
	processed_image = reverse_video(id1, id2)
	histogram_ori = histogram(id1)
	histogram_pro = histogram(id2)
	end_time = datetime.datetime.now()
	processed_time = str(end_time-start_time)
	num_reverse = add_image_reverse(email,id2,datetime.datetime.now())
	processed_image["histogram_original"] = histogram_ori
	processed_image["histogram_processed"] = histogram_pro
	processed_image["processed_time"] = processed_time
	processed_image["reverse_video_times"] = num_reverse
	return jsonify(processed_image)

if __name__ == "__main__":
    app.run()
