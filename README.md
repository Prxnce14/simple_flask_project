This is my simple flask project.
__________________________________ 
Flask is a mirco web framework for python that supports the creation of websites, web applications(APIs) and web services.

An Application Programming Interface(API) acts as a middleman between you frontend and your database. 
An API are sets of routines for buidling software applications. It is a tool for developers to access the functionality of software applications.


The pdf in the root directory consists of the instructions by which this project was focused.



## Starting the project 

1) Create a virtual environment 

Virtualenv <name of your environment>

2) Activating your virtual environment 

<name of your environment>\Scripts\activate 

3) Install your packeds in your require file

pip install -r require.txt


4) Starting your development server

flask --app app.init.py --debug run


## Running the project using Mysql Workbench

Please ensure that you create a user and a database on your local machine. 

Navigate to the .env.sample file and set your DATABASE_URL varaible to the mysql user details


Running the project uding PSQL and SQLAlchemy - Switch to welcome branch ( git checkout welcome )





## LICENSE

[MIT LICENSE](LICENSE)