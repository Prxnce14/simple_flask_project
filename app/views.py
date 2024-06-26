import os
from flask import Flask, request, make_response, jsonify
import mysql.connector
from app import app
from .config import Config



# Function to establish database connection
def get_database_connection():
    try:
        # Retrieve DATABASE_URL from environment variables
        database_url = os.environ.get('DATABASE_URL')
        if not database_url:
            raise ValueError("DATABASE_URL environment variable is not set")
        
        # Parse the database URL
        parts = database_url.split('://')[1].split('@')
        user_pass, host_db = parts[0].split(':'), parts[1].split('/')
        username, password = user_pass[0], user_pass[1]
        host, database = host_db[0], host_db[1]
        
        # Establish the database connection
        con = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=database
        )
        return con
    except Exception as e:
        return None  # Returning None to indicate connection failure
    


@app.route('/hello_world', methods=['GET'])
def hello_world():
    return "hello this is a big world"



@app.route('/get_students', methods = ['GET'])
def get_students():
    try:
        con = get_database_connection()
        if con:
            #this creates a cursor
            cur = con.cursor()
            cur.execute('SELECT * FROM Student')
            stud_list = []
            for student_id, name, address, email in cur:
                student = {}
                student['id'] = student_id
                student['name'] = name
                student['address'] = address
                student['email'] = email
                stud_list.append(student)
            cur.close()
            con.close()
            return stud_list
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    


@app.route('/get_courses', methods = ['GET'])
def get_courses():
    try:
        con = get_database_connection()
        if con:
            #this creates a cursor
            cur = con.cursor()
            cur.execute('SELECT * FROM Course')
            course_list = []
            for course_id, course_name, date_orig in cur:
                course = {}
                course['id'] = course_id
                course['name'] = course_name
                course['date created'] = date_orig
                course_list.append(course)
            cur.close()
            con.close()
            return course_list
    #This allows you to see the exact error encountered
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    


@app.route('/get_enrol', methods= ['GET'])
def get_enrol():
    try:
        con = get_database_connection()
        if con:
            #this cretaes a cursor
            cur = con.cursor()
            cur.execute('SELECT * FROM Enrol')
            enrol_list= []
            for stud_id, course_id, grade in cur:
                enrol = {}
                enrol['student id'] = stud_id
                enrol['course id'] = course_id
                enrol['grade'] = grade
                enrol_list.append(enrol)
            cur.close
            con.close
            return enrol_list
    #This allows you to see the exact error encountered
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    





@app.route('/get_name_address', methods= ['GET'])
def get_name_address():
    try:
        con = get_database_connection()
        if con:
            #this cretaes a cursor
            cur = con.cursor()
            cur.execute('SELECT Name, Address FROM student')
            stud_list= []
            for name, address in cur:
                stud = {}
                stud['name'] = name
                stud['address'] = address
                stud_list.append(stud)
            cur.close
            con.close
            return stud_list
    #This allows you to see the exact error encountered
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    




@app.route('/get_student/<student_id>', methods= ['GET'])
def get_student(student_id):
    try:
        con = get_database_connection()
        if con:
            #this cretaes a cursor
            cur = con.cursor()
            cur.execute(f'SELECT Name, Address, email FROM student WHERE StudentID = {student_id}')
            row = cur.fetchone()
            if row is not None:
                stud_name, address, email = row
                student = {}
                student['name'] = stud_name
                student['address'] = address 
                student['email'] = email
                cur.close()
                con.close()
                return make_response(student, 200)
            else:
                return make_response({'error': 'Student id not found'}, 400)
    except Exception as e:
        return make_response({'error': str(e)}, 400)




@app.route('/get_address/<stud_name>', methods= ['GET'])
def get_address(stud_name):
    try:
        con = get_database_connection()
        if con:
            #this cretaes a cursor
            cur = con.cursor()
            cur.execute(f'SELECT StudentID, Address FROM student WHERE Name = {stud_name}')
            row = cur.fetchone()
            if row is not None:
                stud_id, address = row
                student = {}
                student['student id'] = stud_id
                student['address'] = address 
                cur.close()
                con.close()
                return make_response(student, 200)
            else:
                return make_response({'error': 'Student name not found'}, 400)
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    




@app.route('/get_nameby_address/<address>', methods= ['GET'])
def get_nameby_address(address):
    try:
        con = get_database_connection()
        if con:
            #this cretaes a cursor
            cur = con.cursor()
            cur.execute(f"SELECT Name, Address FROM student WHERE Address = {address} ")
            row = cur.fetchone()
            if row is not None:
                name, address = row
                student = {}
                student['Name'] = name
                student['address'] = address 
                cur.close()
                con.close()
                return make_response(student, 200)
            else:
                return make_response({'error': 'name could not be found'}, 400)
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    
    

    
