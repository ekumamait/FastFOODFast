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

        """ This query creates the Users table """
        create_user_table = """ CREATE TABLE IF NOT EXISTS Users(user_id SERIAL PRIMARY KEY, 
        user_name VARCHAR(100) NOT NULL, user_email VARCHAR(120) NOT NULL, 
        user_password VARCHAR(20) NOT NULL, admin BOOLEAN NOT NULL) """
        self.cur.execute(create_user_table)
        self.conn.commit()

        """ This query creates the Menu table """
        create_menu = """ CREATE TABLE IF NOT EXISTS Menu(meal_id SERIAL PRIMARY KEY, 
        meal_name VARCHAR(100) NOT NULL,meal_description VARCHAR(20) NOT NULL, 
        meal_price VARCHAR(50) NOT NULL) """
        self.cur.execute(create_menu)
        self.conn.commit()

        """ This SQL query creates the Orders table """
        create_user_orders = """ CREATE TABLE IF NOT EXISTS Orders(user_id SERIAL 
        REFERENCES Users (user_id), meal_id SERIAL REFERENCES Menu (meal_id), 
        order_id SERIAL PRIMARY KEY, location VARCHAR(20) NOT NULL, 
        quantity VARCHAR(20) NOT NULL, order_date DATE NOT NULL DEFAULT CURRENT_DATE, status VARCHAR(20)) """
        self.cur.execute(create_user_orders)
        self.conn.commit()
        self.conn.close()


class Users():
    
    def __init__(self, user_name, user_email, user_password):
        self.conn = psycopg2.connect(dbname='fastfoodfast', 
        host='localhost', user='postgres', password='incorrect')
        self.cur = self.conn.cursor()
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password

    def insert_new_user(self, user_name, user_email, user_password):
        """Function to handles user registration"""     
        create = """INSERT INTO Users(user_name, user_email, user_password, admin) 
        VALUES ('{0}', '{1}', '{2}', FALSE);""".format(user_name, 
        user_email, user_password)
        self.cur.execute(create)
        self.conn.commit()
        return True


    def get_all_users(self):
        """Function to fetch all registered users"""
        create = """SELECT * FROM Users;"""
        self.cur.execute(create)
        return True

    def promote_user(self, user_name):
        """Function to promote user to admin"""
        create = """UPDATE Users SET admin = TRUE WHERE ;""" 
        self.cur.execute(create)
        self.conn.commit()
        return True   

      
class Menu():
    
    def __init__(self):
        self.conn = psycopg2.connect(dbname='fastfoodfast', 
        host='localhost', user='postgres', password='incorrect')
        self.cur = self.conn.cursor()


    def insert_new_meal(self, meal_name, meal_description, meal_price):
        """Function to add a new meal to the menu"""
        create = """INSERT INTO Menu(meal_name, meal_description, meal_price) 
        VALUES ('{0}', '{1}', '{2}')""".format(meal_name, 
        meal_description, meal_price)        
        self.cur.execute(create)
        self.conn.commit()
        return True 


    def get_all_meals(self):
        """Function to fetch all meals from the menu"""
        create = """SELECT * FROM Menu;"""
        self.cur.execute(create)
        meals = self.cur.fetchall() 
        return meals


class Orders():

    def __init__(self):
        self.conn = psycopg2.connect(dbname='fastfoodfast', 
        host='localhost', user='postgres', password='incorrect')
        self.cur = self.conn.cursor()


    def place_new_order(self, location, quantity, user_id, meal_id):
        """Function to place an order"""
        create = """INSERT INTO Orders(location, quantity, user_id, meal_id, status) 
        VALUES ('{0}', '{1}', '{2}', '{3}', 'pending')""".format(location, 
        quantity, user_id, meal_id)        
        self.cur.execute(create)
        self.conn.commit()
        return True 


    def get_order_by_id(self, order_id):
        """Function to get an order by id from menu in database""" 
        create = """SELECT * FROM Orders 
        WHERE order_id='{0}'""".format(order_id)
        self.cur.execute(create)
        order = self.cur.fetchone()      
        return order


    def get_all_orders(self, user_id):
        """Function to get all orders of a specific user"""
        create = """SELECT * FROM Orders WHERE user_id='{}'""".format(user_id)
        self.cur.execute(create)
        orders = self.cur.fetchall() 
        return orders


    def edit_specific_order(self, order_id, status, user_id):
        """Function to edit an orders status"""
        create =  """UPDATE Orders SET status='{0}' 
        WHERE order_id='{1}' AND user_id='{2}'""".format(status, order_id, user_id)
        self.cur.execute(create)
        self.conn.commit()
        return True 


    def get_orders(self):
        """Function to get all orders"""
        create = """SELECT * FROM Orders;"""
        self.cur.execute(create)
        orders = self.cur.fetchall() 
        return orders


    def search_user(self, user_name):
        """Function to search Users and return user id"""
        create = """SELECT user_id FROM Users WHERE user_name='{}'""".format(user_name)
        self.cur.execute(create)
        user_id = self.cur.fetchone() 
        return user_id 


    def search_menu(self, meal_name):
        """Function to search menu and return meal id"""
        create = """SELECT meal_id FROM Menu WHERE meal_name='{}'""".format(meal_name)
        self.cur.execute(create)
        meal_id = self.cur.fetchone() 
        return meal_id    
   
# import pdb;pdb.set_trace()

