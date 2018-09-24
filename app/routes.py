""" 
	This is the routes module which 
	contains the application wide endpoints.
"""

from flask import jsonify, request, abort, make_response
from app import app
from app.models import Orders

model = Orders()


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
	return make_response(jsonify({'error': 'incomplete order'}), 400)


@app.route('/')
def index():
	return "Welcome to FastFOODFast"


@app.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
	""" end point for getting all orders """
	if request.method != "GET":
		abort(405)

	customers = model.get_all_orders()
	return make_response(jsonify({'All Orders': customers}), 200)


@app.route('/api/v1/orders/<int:order_id>', methods=['GET'])
def get_single_order(order_id):
	""" end point for getting a single order """
	if request.method != "GET":
		abort(405)

	order = model.get_specific_order(order_id)
	return make_response(jsonify({'msg': order}))


@app.route('/api/v1/orders', methods=['POST'])
def add_single_order():
	""" end point for adding an order """
	if request.method != "POST":
		abort(405)

	new_order = request.get_json()
	model.add_new_order(new_order['meal'],
	new_order['location'], new_order['quantity'])
	return make_response(jsonify({'msg': 'order placed'}), 200)


@app.route('/api/v1/orders/<int:order_id>', methods=['PUT'])
def edit_single_order(order_id):
	""" end point for editting an order """
	if request.method != "PUT":
		abort(405)

	edit_order = request.get_json()
	model.edit_specific_order(edit_order, order_id)
	return make_response(jsonify({'msg': 'Order updated'}), 200)
