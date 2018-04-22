import pymodm
from pymodm import connect
from flask import Flask, jsonify, request
from flask_cors import CORS
#import database_functions
#import models
import datetime
from skimage import exposure
import base64
import numpy as np
import uuid
import os
import math
from skimage import util
import  PIL
app = Flask(__name__)
CORS(app)
connect("mongodb://vcm-3572.vm.duke.edu:27017/imaging_processing")  # open up connection to db  ????


@app.route("/api/histogram_equalization", methods=["POST"])
def store_heart_rate():
    """
        send back the histogram equalization processing result
        """
    r = request.get_json()  # parses the POST request body as JSON
    start = datetime.datetime.now()
    end = datetime.datetime.now()
    process_time = start - end


@app.route("/api/contrast-stretching", methods=["POST"])
def store_heart_rate():
    """
        send back the contrast stretching processing result
        """
    r = request.get_json()  # parses the POST request body as JSON
    start = datetime.datetime.now()
    end = datetime.datetime.now()
    process_time = start - end


@app.route("/api/log_compression", methods=["POST"])
def store_heart_rate():
    """
        send back the log compression processing result
        """
    r = request.get_json()  # parses the POST request body as JSON
    start = datetime.datetime.now()
    end = datetime.datetime.now()
    process_time = start - end


@app.route("/api/reverse_video", methods=["POST"])
def store_heart_rate():
    """
        send back the reverse video processing result
        """
    r = request.get_json()  # parses the POST request body as JSON
    start = datetime.datetime.now()
    end = datetime.datetime.now()
    process_time = start - end

if __name__ == "__main__":
    app.run()