""" Api endpoint logic """

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

from app.models import Database
db = Database()
db.table()

from app import routes
from app.models import Users, Orders, Menu
# import pdb;pdb.set_trace()