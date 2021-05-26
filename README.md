
[![Build Status](https://www.travis-ci.com/VladyslavPodrazhanskyi/departments_application.svg?branch=master)](https://www.travis-ci.com/VladyslavPodrazhanskyi/departments_application?branch=master)
[![codecov](https://codecov.io/gh/VladyslavPodrazhanskyi/departments_application/branch/master/graph/badge.svg)](https://codecov.io/gh/VladyslavPodrazhanskyi/departments_application)


Department application (web application with rest api service.)
Web application created for departments and employees of the company Global Pharma Trade LLC. 

You can see demo version of working application deployed to the heroku server:

https://departmentsemployees.herokuapp.com


The web application allows:

1.display a list of departments and the average salary (calculated automatically) for these departments.
2.display a list of employees in the departments with an indication of the salary 
for each employee and a search field to search for employees born on a certain date 
or in the period between dates
3.change (add / edit / delete) the above data

Application has REST API service for third-party developers that allows
to display list of departments, employees in json format,
change (add / edit / delete) the above data.


Perform following steps to build and run the project:


•	clone this repo:
 $ git clone https://github.com/VladyslavPodrazhanskyi/departments_application.git
•	make project folder current:
$ cd department_application
•	create Python virtual environment:
$ python3 -m venv venv
•	activate virtual environment:
$ source venv/bin/activate
•	install project requirements:
$ pip install -r requirements.txt






