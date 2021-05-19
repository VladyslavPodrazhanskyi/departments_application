# departments_application ! 
# details about project goal in English



[![Build Status](https://www.travis-ci.com/VladyslavPodrazhanskyi/departments_application.svg?branch=master)](https://www.travis-ci.com/VladyslavPodrazhanskyi/departments_application)

[![codecov](https://codecov.io/gh/VladyslavPodrazhanskyi/departments_application/branch/master/graph/badge.svg)](https://codecov.io/gh/VladyslavPodrazhanskyi/departments_application)


Department managing app built with Flask. Lets user add, edit, delete departments and their employees. Calculates and displays average salary for each department, gives user an ability to filter employees by range of birth dates.

Perform following steps to build the project.

Clone this repo:

$ git clone https://github.com/andrsko/department-app
Make project folder current:

$ cd department-app
Create Python virtual environment:

$ python3 -m venv venv
Activate virtual environment:

$ source venv/bin/activate
Install project production requirements:

$ pip install -r requirements/prod.txt
Start Gunicorn service for web service:

$ gunicorn -c ./webservice.conf.py
Start Gunicorn service for web app:

$ gunicorn -c ./webapp.conf.py
After that the web service and the web app will be available on http://127.0.0.1:8000 and http://127.0.0.1:3000 respectively, with logs being written to "gunicorn.log".