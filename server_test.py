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

app = Flask(__name__)
CORS(app)
connect("mongodb://vcm-3551.vm.duke.edu:27017/image-app")  # open up connection to db  ????


@app.route("/api/histogram_equalization", methods=["POST"])
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
	# except AssertionError as e:
	#	logging.warning("Incorrect image type given: {}".format(e))
 	#	err = {"error": "Incorrect image type given"}
 	#	return jsonify(err), 400
	if already_user(email):
		u_vals = add_uploadimage(email, image = image_new, 
					 time=datetime.datetime.now())
	else:
		u_vals = create_user(email)
		u_vals = add_uploadimage(email, image = image_new,
					 time=datetime.datetime.now())
	logging.debug("adding new image to user: {}".format(u_vals))
	return jsonify(u_vals),200

if __name__ == "__main__":
    app.run()
