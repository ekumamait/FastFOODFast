
##### WELCOME TO FastFOODFast
<<<<<<< HEAD
------------

[![Build Status](https://travis-ci.org/ekumamait/FastFOODFast.svg?branch=ft-challenge-three)](https://travis-ci.org/ekumamait/FastFOODFast) [![Coverage Status](https://coveralls.io/repos/github/ekumamait/FastFOODFast/badge.svg?branch=ft-challenge-three)](https://coveralls.io/github/ekumamait/FastFOODFast?branch=ft-challenge-three) [![Maintainability](https://api.codeclimate.com/v1/badges/91ef436eedd5ec2532e6/maintainability)](https://codeclimate.com/github/ekumamait/FastFOODFast/maintainability)
=======

------------

[![Build Status](https://travis-ci.org/ekumamait/FastFOODFast.svg?branch=api)](https://travis-ci.org/ekumamait/FastFOODFast) [![Coverage Status](https://coveralls.io/repos/github/ekumamait/FastFOODFast/badge.svg?branch=api)](https://coveralls.io/github/ekumamait/FastFOODFast?branch=api) [![Maintainability](https://api.codeclimate.com/v1/badges/91ef436eedd5ec2532e6/maintainability)](https://codeclimate.com/github/ekumamait/FastFOODFast/maintainability) 
>>>>>>> fd785df93e7e94d95f11562329ab42e870685ac1

------------

##### TABLE OF CONTENT;

------------

- [x] **DESCRIPTION**
- [x] **PROJECT SETUP**
- [x] **AVAILABLE ROUTES**
- [x] **TESTS**
- [x] **PROJECT DEMO**

------------

###### :page_facing_up: DESCRIPTION;

<<<<<<< HEAD
This is an online food order and delivery service app for a restaurant where registered customers can order daily meals from the famous menu and have the meals delivered to them at home or office. The main focus of this build in its present is the API using a database for persistant data storage.
=======
This is an online food order and delivery service app for a restaurant where registered customers can order daily meals from the famous menu and have the meals delivered to them at home or office. The main focus of this build in its present is the API using data structures for non persistant data storage.
>>>>>>> fd785df93e7e94d95f11562329ab42e870685ac1

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
<<<<<<< HEAD
| /api/v2/auth/sign_up | POST | `signs up a user `  |
| /api/v2/auth/login | POST | `Logs in a user` |
| /api/v2/users/orders | POST | `place a new order`  |
| /api/v2/users/orders| GET | `Fetch all logged in user's orders` |
| /api/v2/orders| GET | `Fetch all users orders` |
| /api/v2/orders/order_id| GET | `Fetch specific order` |
| /api/v2/orders/order_id| PUT | `Update the status of an order` |
| /api/v2/menu| GET | `Fetch Menu` |
| /api/v2/menu| POST | `Add meal to the Menu` |
| /api/v2/users/user_id| PUT | `Promote user role to admin` |
=======
| /api/v1/orders | GET | `Fetches all orders created`  |
| /api/v1/orders/int:order_id | GET | `Fetches a specific order by id` |
| /api/v1/orders | POST | `add a new order`  |
| /api/v1/orders/int:order_id'| PUT | `edit a single order` |
>>>>>>> fd785df93e7e94d95f11562329ab42e870685ac1

------------

###### :microscope: TESTS;

- [x] Tests for routes 

- command to run tests:
    ` nosetests -v `

- command to run tests with coverage:
<<<<<<< HEAD
    ` nosetests -v --with-coverage ` 
      
=======
    ` nosetests -v --with-coverage `    
>>>>>>> fd785df93e7e94d95f11562329ab42e870685ac1
------------

###### Project Demo;

<<<<<<< HEAD
Here is the link to the Demo:
=======
- Here is the link to the App Demo: 
>>>>>>> fd785df93e7e94d95f11562329ab42e870685ac1
https://ekumamaits-fastfoodfast.herokuapp.com/

------------

