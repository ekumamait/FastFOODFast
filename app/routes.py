""" 
	This is the routes module which 
	contains the application wide endpoints.
"""

from flask import jsonify, request, abort, make_response
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity
from app import app
from app.models import Users, Orders, Menu
import re
import datetime

ticket = Orders()
meal = Menu()
customers = Users()


@app.errorhandler(404)
def not_found(error):
    """ Custom HTTP 404 Not found error """
    return make_response(jsonify({'error': 'Nothing found'}), 404)


@app.errorhandler(405)
def not_allowed(error):
	""" Custom HTTP 405 Method Not Allowed error """
	return make_response(jsonify
	({'error': 'You are trying to use a wrong HTTP Method'}), 405)


@app.errorhandler(500)
def server_down(error):
	""" Custom HTTP 500 Method server error """
	return make_response(jsonify
	({'error': 'server went down'}), 500)


@app.errorhandler(400)
def bad_request(error):
	""" Custom HTTP 400 Bad Request error """
	return make_response(jsonify({'error': 'incomplete Request'}), 400)


@app.route('/api/v2/auth/sign_up', methods = ['POST'])
def sign_up():
	""" end point for signing up a user """
	if request.method != "POST":
		abort(405)

	new_user = request.get_json()

	data = customers.search_user_name(new_user['user_name'])
	
	if not data:

		if new_user['user_name'] is not None and new_user['user_name'].strip() == "":
			return make_response(jsonify({"msg": "username can not be blank "}), 401)

		if new_user['user_email'] is not None and new_user['user_email'].strip() == "":
			return make_response(jsonify({"msg": "useremail can not be blank "}), 401)

		if new_user['user_password'] is not None and new_user['user_password'].strip() == "":
			return make_response(jsonify({"msg": "userpassword can not be blank "}), 401)

		if not re.match(r"[^@]+@[^@]+\.[^@]+", new_user['user_email']):
			return make_response(jsonify({"msg": "incorrect email format "}), 401)

		customers.insert_new_user(new_user["user_name"], new_user["user_email"], 
		new_user["user_password"])
		return jsonify({'msg': 'account created'}), 201

	else:
		return make_response(jsonify({"msg": "user already exists"}), 401)			
		

@app.route('/api/v2/auth/login', methods=['POST'])
def login():
	""" end point for logging in a user """
	user = request.json
	
	if not user['Username']:
		return jsonify({"msg": "Missing username parameter"}), 400
	if not user['Password']:
		return jsonify({"msg": "Missing password parameter"}), 400

	if user['Username'] is not None and user['Username'].strip() == "":
			return jsonify({"msg": "username can not be blank "}), 401		

	if user['Password'] is not None and user['Password'].strip() == "":
			return jsonify({"msg": "userpassword can not be blank "}), 401		

	password = customers.search_user_password(user['Password'])

	if not password:
		return jsonify({"msg": "wrong password"}), 401
	
	userid = ticket.search_user(user['Username'])
	role = customers.search_user_role(user['Username'])

	user_info = {'userid': userid,'role': role}
	expires = datetime.timedelta(hours=4)
	access_token = create_access_token(identity=user_info, expires_delta=expires)
	return jsonify(access_token=access_token, message='succefully'), 200


@app.route('/api/v2/users/orders', methods=['POST'])
@jwt_required
def add_single_order():
	""" end point for placing an order """
	if request.method != "POST":
		abort(405)

	new_order = request.get_json()
	user_id = get_jwt_identity()['userid']['user_id']
	
	meal_id = ticket.search_menu(new_order['meal_name'])
	# import pdb;pdb.set_trace()
	if meal_id is None:
		return 'meal does not exist'
	ticket.place_new_order(new_order['location'], 
	new_order['quantity'], user_id, meal_id['meal_id'])
	return make_response(jsonify({'msg': 'order placed'}), 201)


@app.route('/api/v2/users/orders', methods=['GET'])
@jwt_required
def get_my_orders():
	""" end point for getting order history of a specific user """
	if request.method != "GET":
		abort(405)
		
	user_id = get_jwt_identity()['userid']['user_id']
	customers = ticket.get_all_orders(user_id)
	return make_response(jsonify({'All Orders': customers}), 200)


@app.route('/api/v2/orders', methods=['GET'])
@jwt_required
def all_orders():
	""" end point for fetching all available orders """
	if request.method != "GET":
		abort(405)

	current_user = get_jwt_identity()['role']['admin']
	if current_user is True: 
		all = ticket.get_orders()
		return make_response(jsonify({'All Orders': all}), 200)
	return make_response(jsonify({'error': 'not authorized'}), 401)    


@app.route('/api/v2/orders/<int:order_id>', methods=['GET'])
@jwt_required
def get_single_order(order_id):
	""" end point for fetching a single order by order id """
	if request.method != "GET":
		abort(405)

	current_user = get_jwt_identity()['role']['admin']
	if current_user is True:
		order = ticket.get_order_by_id(order_id)
		return make_response(jsonify({'msg': order}), 200)
	return make_response(jsonify({'error': 'not authorized'}), 401) 	


@app.route('/api/v2/orders/<int:order_id>', methods=['PUT'])
@jwt_required
def edit_single_order(order_id):
	""" end point for editting a specific order """
	if request.method != "PUT":
		abort(405)

	edit_order = request.get_json()
	current_user = get_jwt_identity()['role']['admin']
	if current_user is True:
		ticket.edit_specific_order(order_id, edit_order['status'])
		return make_response(jsonify({'msg': 'Order updated'}), 201)
	return make_response(jsonify({'error': 'not authorized'}), 401)	


@app.route('/api/v2/menu', methods=['GET'])
@jwt_required
def get_menu():
    """ end point for fetching the menu """
    if request.method != "GET":
        abort(405)

    current_menu = meal.get_all_meals()
    return jsonify({'message': current_menu}), 200


@app.route('/api/v2/menu', methods=['POST'])
@jwt_required
def add_to_menu():
	""" end point for adding a new meal to the menu """
	if request.method != "POST":
		abort(405)

	new_meal = request.get_json()
	current_user = get_jwt_identity()['role']['admin']
	
	if current_user is True: 
		meal.insert_new_meal(new_meal['meal_name'], new_meal['meal_description'], new_meal['meal_price'])
		return jsonify({'message': "menu item added"}), 201	
	return make_response(jsonify({'error': 'not authorized'}), 401) 


@app.route('/api/v2/users/<int:user_id>', methods=['PUT'])
def access(user_id):
	""" end point for editting an order """
	if request.method != "PUT":
		abort(405)

	customers.promote_user(user_id)
	return make_response(jsonify({'msg': 'role updated'}), 201) 	

