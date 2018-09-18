""" Api endpoint logic """

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

from api import routes 