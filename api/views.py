from flask import jsonify, request  
from datetime import datetime
from api import app

date = datetime.now()
now = date.strftime("%d-%m-%Y %H:%M")

Orders = []

@app.route('/')
def index():
	return "Welcome to FastFOODFast"

@app.route('/api/v1/orders', methods = ['GET'] )
def all_orders():

	return jsonify(Orders)

@app.route('/api/v1/orders/<int:order_id>', methods = ['GET'] )
def single_order(order_id):

	order = [order for order in Orders if order['order_id'] == order_id]
	return jsonify({'order': order[0]})

@app.route('/api/v1/orders', methods = ['POST'] )
def add_order():

	new_order = request.get_json() 
	new_order['date'] = now
	Orders.append(new_order)
	id = 1
	for order in Orders:
		order['order_id'] = id
		id += 1
	return jsonify({'orders': Orders})

@app.route('/api/v1/orders/<int:order_id>', methods = ['PUT'] )
def edit_order(order_id):
	new_order = request.get_json()
	order = [order for order in Orders if order['order_id'] == order_id]
	for order in Orders:
		if order['order_id'] == order_id:
			order['status'] = new_order['status']
			return jsonify({'200' : 'Order status updated'})
	return jsonify({'404':'Resource not found'})