""" This is the routes module which contains the application wide endpoints."""

from flask import jsonify, request, abort, make_response  
from api import app
from api.models import Orders

model = Orders()

@app.errorhandler(404) 
def not_found(error):   
    """ Customised HTTP 404 Not found error """
    return make_response(jsonify( { 'error': '  :(  Oops Nothing found  ' } ), 404)

@app.errorhandler(405) 
def not_allowed(error):   
    """ Customised HTTP 405 Method Not Allowed error """
    return make_response(jsonify( { 'error': '  :(  Oops Your trying to use a wrong HTTP Method  ' } ), 405)

@app.errorhandler(400) 
def bad_request(error):   
    """ Customised HTTP 400 Bad Request error """
    return make_response(jsonify( { 'error': '  :(  BAD REQUEST  ' } ), 400)

@app.errorhandler(401)
def unauthorised(error):
    """ Customised HTTP 401 unauthorised error """
    return make_response(jsonify({'error':'You are not logged in! Please first login'}),401)

@app.errorhandler(500)
def internal_server_error(error):
    """ Customised HTTP 500 internal server error """
    return make_response(jsonify({'failed':'The server run into an error'}),500)

@app.route('/')
def index():
	return "Welcome to FastFOODFast"

@app.route('/api/v1/orders', methods = ['GET'] )
def all_orders():
	""" end point for getting all orders """
	if request.method != "GET":
		abort(405)

	customers = model.get_all_orders()

	return jsonify({'All Orders': customers})

@app.route('/api/v1/orders/<int:order_id>', methods = ['GET'] )
def single_order(order_id):
	""" end point for getting a single order """
	if request.method != "GET":
		abort(405)

	order = model.get_single_order(order_id)

	return jsonify({'msg': order})

@app.route('/api/v1/orders', methods = ['POST'] )
def add_order():
	""" end point for adding an order """
	if request.method != "POST":
		abort(405)

	new_order = request.get_json()
	model.add_new_order(new_order['meal'], new_order['location'], new_order['quantity']) 

	return jsonify({'msg': 'order placed'})

@app.route('/api/v1/orders/<int:order_id>', methods = ['PUT'] )
def edit_order(order_id):
	""" end point for editting an order """
	if request.method != "PUT":
		abort(405)

	edit_order = request.get_json()
	model.edit_order(edit_order, order_id)

	return jsonify({'msg' : 'Order status updated'}), 200
