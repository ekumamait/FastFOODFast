
##### WELCOME TO FastFOODFast

------------

------------

##### TABLE OF CONTENT;

------------

- [x] **DESCRIPTION**
- [x] **PROJECT SETUP**
- [x] **AVAILABLE ROUTES**
- [ ] **TESTS**
- [ ] **PROJECT DEMO**

------------

###### :page_facing_up: DESCRIPTION;

This is an online food order and delivery service app for a restaurant where registered customers can order daily meals from the famous menu and have the meals delivered to them at home or office. The main focus of this build in its present is the API using a database for persistant data storage.

------------

##### PROJECT SETUP

------------

1. Clone the Repository
`https://github.com/ekumamait/FastFOODFast`

2. Navigate to the application directory
`cd FastFOODFast`

3. install all dependencies
`pip install -r requirements.txt`

4. activate virtual environment
`source venv\Scripts\activate`

5. Run the application
`python run.py`

------------

###### AVAILABLE ROUTES;

|  EndPoint   | Methods | Functionality |
| ------------ |------------| ------------ |
| /api/v2/auth/sign_up | POST | `signs up a user `  |
| /api/v2/auth/login | POST | `Logs in a user` |
| /api/v2/users/orders | POST | `place a new order`  |
| /api/v2/users/orders| GET | `Fetch all logged in user's orders` |
| /api/v2/orders| GET | `Fetch all users orders` |
| /api/v2/orders/order_id| GET | `Fetch specific order` |
| /api/v2/orders/order_id| PUT | `Update the status of an order` |
| /api/v2/menu| GET | `Fetch Menu` |
| /api/v2/menu| POST | `Add meal to the Menu` |

------------

###### :microscope: TESTS;

Pending...   
------------

###### Project Demo;

Pending...
------------

