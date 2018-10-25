""" Api endpoint logic """

from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity 

app = Flask(__name__, static_url_path="/",
            static_folder="../UI",
            template_folder="../UI")
CORS(app) 


app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

from app.models import Database
db = Database()
db.table()

from app import routes
from app.models import Users, Orders, Menu
