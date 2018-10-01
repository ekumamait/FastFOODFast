""" 
	This is the routes module which 
	contains the application wide endpoints.
"""

from flask import jsonify, request, abort, make_response
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity
from app import app
from app.models import Users, Orders, Menu, Database

db = Orders()
meal = Menu()
TS = Database()


@app.errorhandler(404)
def not_found(error):
    """ Custom HTTP 404 Not found error """
    return make_response(jsonify({'error': 'Nothing found'}), 404)


@app.errorhandler(405)
def not_allowed(error):
	""" Custom HTTP 405 Method Not Allowed error """
	return make_response(jsonify
	({'error': 'You are trying to use a wrong HTTP Method'}), 405)


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
	customers = Users(new_user['user_name'], new_user['user_password'],new_user['user_email'])	
	
	customers.insert_new_user(new_user["user_name"], new_user["user_email"], 
	new_user["user_password"])
	return jsonify({'msg': 'account created'}), 200


@app.route('/api/v2/auth/login', methods=['POST'])
def login():
	""" end point for logging in a user """
	user = request.json
	
	if not user['Username']:
		return jsonify({"msg": "Missing username parameter"}), 400
	if not user['Password']:
		return jsonify({"msg": "Missing password parameter"}), 400

	userid = db.search_user(user['Username'])

	access_token = create_access_token(identity=userid)
	return jsonify(access_token=access_token), 200


@app.route('/api/v2/users/orders', methods=['POST'])
@jwt_required
def add_single_order():
	""" end point for adding an order """
	if request.method != "POST":
		abort(405)

	new_order = request.get_json()
	user_id = get_jwt_identity()[0]
	meal_id = db.search_menu(new_order['meal_name'])
	db.place_new_order(new_order['location'], 
	new_order['quantity'], user_id, meal_id[0])
	return make_response(jsonify({'msg': 'order placed'}), 200)


@app.route('/api/v2/users/orders', methods=['GET'])
@jwt_required
def get_my_orders():
	""" end point for getting all orders of a specific user """
	if request.method != "GET":
		abort(405)
		
	user_id = get_jwt_identity()[0]
	customers = db.get_all_orders(user_id)
	return make_response(jsonify({'All Orders': customers}), 200)


@app.route('/api/v2/orders', methods=['GET'])
def all_orders():
	""" end point for getting all orders of a specific user """
	if request.method != "GET":
		abort(405)
	
	customers = db.get_orders()
	return make_response(jsonify({'All Orders': customers}), 200)    


@app.route('/api/v2/orders/<int:order_id>', methods=['GET'])
def get_single_order(order_id):
	""" end point for getting a single order """
	if request.method != "GET":
		abort(405)

	order = db.get_order_by_id(order_id)
	return make_response(jsonify({'msg': order}))


@app.route('/api/v2/orders/<int:order_id>', methods=['PUT'])
def edit_single_order(order_id):
    """ end point for editting an order """
    if request.method != "PUT":
        abort(405)

    edit_order = request.get_json()
    db.edit_specific_order(order_id, edit_order['status'])
    return make_response(jsonify({'msg': 'Order updated'}), 200)

@app.route('/api/v2/menu', methods=['GET'])
def get_menu():
    """ end point for getting the menu """
    if request.method != "GET":
        abort(405)

    current_menu = meal.get_all_meals()
    return jsonify({'message': current_menu}), 200

@app.route('/api/v2/menu', methods=['POST'])
def add_to_menu():
	""" end point for addin to the menu """
	if request.method != "POST":
		abort(405)

	new_meal = request.get_json()
	
	meal.insert_new_meal(new_meal['meal_name'], new_meal['meal_description'], new_meal['meal_price'])
	return jsonify({'message': "menu item added"}), 200	

@app.route('/api/v2/users/<int:user_id>', methods=['PUT'])
def access(user_id):
	""" end point for editting an order """
	if request.method != "PUT":
		abort(405)

	TS.promote_user(user_id)
	return make_response(jsonify({'msg': 'role updated'}), 200) 	



