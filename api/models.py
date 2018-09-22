""" This is the Orders module which associates the endpoints to their functions."""
from flask import request, abort, make_response
from datetime import datetime

date = datetime.now()
now = date.strftime("%d-%m-%Y %H:%M")

class Orders:
    """ This is the Orders class and it's functions """
    def __init__(self):
        self.order = {}
        self.orders = []
        
    def add_new_order(self, meal, location, quantity):
        """ This function places an order """
        self.order = {'meal': meal, 'location': location, 'quantity': quantity}
        """ function places an order """
        
        if meal == '' or meal == ' ' :
            return abort(400)    
        elif location == '' or location == ' ':
            return abort(400)
        elif quantity == '' or quantity == ' ':
            return abort(400)    
        else:    
            self.order['date'] = now
            self.orders.append(self.order)
            id = 1
            for order in self.orders:
                order['order_id'] = id
                id += 1

    def get_all_orders(self):
       """ This function returns all orders """ 

       return self.orders

    def get_specific_order(self, order_id):
        """ This function returns an order specified by an order_id """
        order = [order for order in self.orders if order['order_id'] == order_id]
        if not order:
            result = ('message: order not found, please check id'), 400 
            return result
        else:    
            return order
   
    def edit_specific_order(self, edit_order, order_id):
        """ This function modifies an order based on order_id """
        if not order_id:
            return abort(400)
        else:    
            for order in self.orders:
                if order['order_id'] == order_id:
                    self.orders.remove(order)
                    edit_order['order_id'] = order_id
                    self.orders.append(edit_order)
        
        
