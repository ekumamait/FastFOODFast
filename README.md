
##### WELCOME TO FastFOODFast

[![Coverage Status](https://coveralls.io/repos/github/ekumamait/FastFOODFast/badge.svg?branch=api)](https://coveralls.io/github/ekumamait/FastFOODFast?branch=api) [![Build Status](https://travis-ci.org/ekumamait/FastFOODFast.svg?branch=api)](https://travis-ci.org/ekumamait/FastFOODFast)

------------

##### TABLE OF CONTENT;

------------

- [x] **DESCRIPTION**
- [x] **PROJECT SETUP**
- [x] **AVAILABLE ROUTES**
- [x] **TESTS**
- [ ] **PROJECT DEMO**

------------

###### :page_facing_up: DESCRIPTION;

This is an online food order and delivery service app for a restaurant where registered customers can order daily meals from the famous menu and have the meals delivered to them at home or office. The main focus of this build in its present is the User Interface of the application.

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
| /api/v1/orders | GET | `Fetches all orders created`  |
| /api/v1/orders/int:order_id | GET | `Fetches a specific order by id` |
| /api/v1/orders | POST | `add a new order`  |
| /api/v1/orders/int:order_id'| PUT | `edit a single order` |

------------

###### :microscope: TESTS;

- [x] Tests for routes 
- [ ] Tests for models

- command to run tests:
    ` nosetests -v `
------------

###### Project Demo;

- Pending....

------------

