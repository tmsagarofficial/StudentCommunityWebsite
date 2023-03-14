import mysql.connector,pymysql
from mysql.connector import errorcode
from flask import Flask, request,render_template,redirect

app = Flask(__name__)

try:
    cnx = mysql.connector.connect(user='root', password='qwe123qwe',
                                  host='localhost',
                                  database='vtech')
    print("Connected to database")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
# configure database connection
db_host = 'localhost'
db_user = 'root'
db_pass = 'qwe123qwe'
db_name = 'vtech'

@app.route('/')
def login():
    return render_template('signlog.html')

@app.route('/signup')
def signup():
    name = request.form['name']
    em = request.form['email']
    passw = request.form['password']

    # Insert the data into the MySQL database
    try:
        cursor = cnx.cursor()
        add_button = ("INSERT INTO login1 "
                      "(name,email,pass) "
                      "VALUES (%s, %s)")
        data = (name,em,passw)
        cursor.execute(add_button, data)
        cnx.commit()
        cursor.close()
        print("Button data inserted successfully")
    except mysql.connector.Error as err:
        print("Error inserting button data: {}".format(err))
        cnx.rollback()

    # Redirect the user back to the form page
    return render_template('index.html')