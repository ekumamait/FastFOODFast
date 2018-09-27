""" 
	This is the models module which 
	contains the application database connection logic and queries.
"""
import psycopg2
 
class Database:
    def __init__(self):
        self.conn = psycopg2.connect(dbname='fastfoodfast', 
        host='localhost', user='postgres', password='incorrect')
        self.cur = self.conn.cursor()

    def table(self):
        create_user_table = """ CREATE TABLE IF NOT EXISTS Users(user_id SERIAL PRIMARY KEY, 
        user_name VARCHAR(100) NOT NULL, user_email VARCHAR(120) NOT NULL, 
        user_password VARCHAR(20) NOT NULL, confirm_password VARCHAR(20) NOT NULL) """
        self.cur.execute(create_user_table)
        self.conn.commit()

        create_menu = """ CREATE TABLE IF NOT EXISTS Menu(meal_id SERIAL PRIMARY KEY, 
        meal_name VARCHAR(100) NOT NULL,meal_description VARCHAR(20) NOT NULL, 
        meal_price VARCHAR(50) NOT NULL) """
        self.cur.execute(create_menu)
        self.conn.commit()

        create_user_orders = """ CREATE TABLE IF NOT EXISTS Orders(user_id SERIAL 
        REFERENCES Users (user_id), meal_id SERIAL REFERENCES Menu (meal_id), 
        order_id SERIAL PRIMARY KEY, location VARCHAR(20) NOT NULL, 
        quantity VARCHAR(20) NOT NULL) """
        self.cur.execute(create_user_orders)
        self.conn.commit()
        self.conn.close()

class Users():
    def __init__(self):
        self.conn = psycopg2.connect(dbname='fastfoodfast', 
        host='localhost', user='postgres', password='incorrect')
        self.cur = self.conn.cursor()

    def insert_new_user(self, user_name, user_email, user_password, confirm_password):
        """A function to create a new user to the database"""
        create = """INSERT INTO Users(user_name, user_email, user_password, confirm_password) 
        VALUES ('{0}', '{1}', '{2}', '{3}');""".format(user_name, user_email, user_password, confirm_password)
        self.cur.execute(create)
        self.conn.commit()
        return True


class Menu():
    def __init__(self):
        self.conn = psycopg2.connect(dbname='fastfoodfast', 
        host='localhost', user='postgres', password='incorrect')
        self.cur = self.conn.cursor()


    def insert_new_meal(self, meal_id, meal_name, meal_description, meal_price):
        """A function to place a new meal to the menu in database"""
        create = """INSERT INTO Events(meal_id, meal_name, meal_description, meal_price) 
        VALUES ('{0}', '{1}', '{2}', '{3}')""".format(meal_id, meal_name, 
        meal_description, meal_price)        
        self.cur.execute(create)
        self.conn.commit()
        return True 


    def get_all_meals(self):
        """A function to get all meals in the menu in database"""
        create = """SELECT * FROM Menu;"""
        self.cur.execute(create)
        return True


class Orders():
    def __init__(self):
        self.conn = psycopg2.connect(dbname='fastfoodfast', 
        host='localhost', user='postgres', password='incorrect')
        self.cur = self.conn.cursor()

    def place_new_order(self, meal_name, location, quantity, user_id, meal_id):
        """A function to place and order"""
        create = """INSERT INTO Orders(meal_name, location, quantity, user_id, event_id) 
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')""".format(meal_name, 
        location, quantity, user_id, meal_id)        
        self.cur.execute(create)
        self.conn.commit()
        return True 

    def get_order_by_id(self, ticket_id, user_id):
        """A function to get an order by id from menu in database""" 
        create = """SELECT * FROM Tickets 
        WHERE ticket_id='{0}' AND user_id='{1}'""".format(ticket_id, user_id)
        self.cur.execute(create)
        tickets = self.cur.fetchall()      
        return tickets

    def get_all_orders(self, user_id):
        """A function to get all orders of a specific user"""
        create = """SELECT * FROM Tickets WHERE user_id='{}'""".format(user_id)
        self.cur.execute(create)
        tickets = self.cur.fetchall() 
        return tickets

    def edit_specific_order(self, order_id, status, user_id):
        """A function to edit an orders status"""
        create =  """UPDATE Orders SET status='{0}' 
        WHERE order_id='{1}' AND user_id='{2}'""".format(status, order_id, user_id)
        self.cur.execute(create)
        self.conn.commit()
        return True    
   
# import pdb;pdb.set_trace()

