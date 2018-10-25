<<<<<<< HEAD
""" 
	This is the routes module which 
	contains the application wide endpoints.
"""

from flask import jsonify, request, abort, make_response, render_template, send_from_directory
from flask_jwt_extended import JWTManager, jwt_required, create_access_token,get_jwt_identity
from app import app
from app.models import Users, Orders, Menu
import re
import datetime
from flasgger import Swagger, swag_from


ticket = Orders()
meal = Menu()
customers = Users()

swagger = Swagger(app)


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


@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")			


@app.route('/js/<path:filename>', methods=['GET'])
def js(filename):
	return send_from_directory("../UI/js", filename)


@app.route('/css/<path:filename>', methods=['GET'])
def css(filename):
	return send_from_directory("../UI/css", filename)


@app.route('/img/<path:filename>', methods=['GET'])
def img(filename):
	return send_from_directory("../UI/img", filename)


@app.route('/api/v2/auth/sign_up', methods = ['POST'])
@swag_from('../Docs/signup.yml')
def sign_up():
	""" end point for signing up a user """

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
@swag_from('../Docs/login.yml')
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
	return jsonify(access_token=access_token, message='succefully', role=role), 200


@app.route('/api/v2/users/orders', methods=['POST'])
@jwt_required
def add_single_order():
	""" end point for placing an order """

	new_order = request.get_json()
	
	user_id = get_jwt_identity()['userid']['user_id']
	if new_order is None:
		return abort(400)
	meal_id = ticket.search_menu(new_order['meal_name'])
	
	if meal_id is None:
		return 'meal does not exist'
	ticket.place_new_order(new_order['location'], 
	new_order['quantity'], user_id, meal_id['meal_id'])
	return make_response(jsonify({'msg': 'order placed'}), 201)


@app.route('/api/v2/users/orders', methods=['GET'])
@jwt_required
def get_my_orders():
	""" end point for getting order history of a specific user """
		
	user_id = get_jwt_identity()['userid']['user_id']
	customers = ticket.get_all_orders(user_id)
	return make_response(jsonify({'All Orders': customers}), 200)


@app.route('/api/v2/orders', methods=['GET'])
@jwt_required
def all_orders():
	""" end point for fetching all available orders """

	current_user = get_jwt_identity()['role']['admin']
	if current_user is True: 
		all = ticket.get_orders()
		return make_response(jsonify({'All Orders': all}), 200)
	return make_response(jsonify({'error': 'not authorized'}), 401)    


@app.route('/api/v2/orders/<int:order_id>', methods=['GET'])
@jwt_required
def get_single_order(order_id):
	""" end point for fetching a single order by order id """

	current_user = get_jwt_identity()['role']['admin']
	if current_user is True:
		order = ticket.get_order_by_id(order_id)
		return make_response(jsonify({'msg': order}), 200)
	return make_response(jsonify({'error': 'not authorized'}), 401) 	


@app.route('/api/v2/orders/<int:order_id>', methods=['PUT'])
@jwt_required
def edit_single_order(order_id):
	""" end point for editting a specific order """

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

    current_menu = meal.get_all_meals()
    return jsonify({'message': current_menu}), 200


@app.route('/api/v2/menu', methods=['POST'])
@jwt_required
def add_to_menu():
	""" end point for adding a new meal to the menu """

	new_meal = request.get_json()
	
	current_user = get_jwt_identity()['role']['admin']
	
	if current_user is True: 
		if not new_meal['meal_name']:
			return jsonify({"msg": "Missing username parameter"}), 400
		if not new_meal['meal_description']:
			return jsonify({"msg": "Missing password parameter"}), 400
		meal.insert_new_meal(new_meal['meal_name'], new_meal['meal_description'], new_meal['meal_price'])
		return jsonify({'message': "menu item added"}), 201	
	return make_response(jsonify({'error': 'not authorized'}), 401) 


@app.route('/api/v2/users/<int:user_id>', methods=['PUT'])
def access(user_id):
	""" end point for editting an order """

	customers.promote_user(user_id)
	return make_response(jsonify({'msg': 'role updated'}), 201) 	

=======
""" This is the routes module which contains the application wide endpoints."""

from flask import jsonify, request, abort, make_response  
from app import app
from app.models import Orders

model = Orders()

@app.errorhandler(404) 
def not_found(error):   
    """ Customised HTTP 404 Not found error """
    return make_response(jsonify( { 'error': 'Nothing found' } ), 404)

@app.errorhandler(405) 
def not_allowed(error):   
    """ Customised HTTP 405 Method Not Allowed error """
    return make_response(jsonify( { 'error': 'You are trying to use a wrong HTTP Method' } ), 405)

@app.errorhandler(400) 
def bad_request(error):   
    """ Customised HTTP 400 Bad Request error """
    return make_response(jsonify( { 'error': 'incomplete order' } ), 400)

@app.route('/')
def index():
	return "Welcome to FastFOODFast"

@app.route('/api/v1/orders', methods = ['GET'] )
def all_orders():
	""" end point for getting all orders """
	if request.method != "GET":
		abort(405)

	customers = model.get_all_orders()

	return make_response(jsonify({'All Orders': customers}), 200)

@app.route('/api/v1/orders/<int:order_id>', methods = ['GET'] )
def single_order(order_id):
	""" end point for getting a single order """
	if request.method != "GET":
		abort(405)

	order = model.get_specific_order(order_id)

	return make_response(jsonify({'msg': order}), 200)

@app.route('/api/v1/orders', methods = ['POST'] )
def add_order():
	""" end point for adding an order """
	if request.method != "POST":
		abort(405)

	new_order = request.get_json()
	model.add_new_order(new_order['meal'], new_order['location'], new_order['quantity']) 
	
	return make_response(jsonify({'msg': 'order placed'}), 200)

@app.route('/api/v1/orders/<int:order_id>', methods = ['PUT'] )
def edit_order(order_id):
	""" end point for editting an order """
	if request.method != "PUT":
		abort(405)

	edit_order = request.get_json()
	model.edit_specific_order(edit_order, order_id)

	return make_response(jsonify({'msg' : 'Order updated'}), 200)
>>>>>>> fd785df93e7e94d95f11562329ab42e870685ac1
