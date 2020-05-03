from flask import Flask,request,jsonify
from flask_cors import CORS
application=Flask(__name__)
CORS(application)
from api import routes
from api import database
from api.database import db