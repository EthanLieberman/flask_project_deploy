import bcrypt
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import MyCustomDB, app
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')




class User:                         # singular instance of...
    def __init__(self,data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.admin = data['admin']






    @classmethod
    def get_one_username(cls, data):
        query = "SELECT * FROM users WHERE username = %(username)s"
        results = connectToMySQL(MyCustomDB).query_db(query, data)     
        return cls(results[0])


    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(MyCustomDB).query_db(query, data)
        if not results:
            return False
        return cls(results[0])


    @classmethod
    def save_account(cls, data):
        hashed = {
            'username': data['username'],
            'email': data['email'],
            'password': bcrypt.generate_password_hash(data['password'])
        }
        query = "INSERT INTO users ( username , email , password , created_at , updated_at , admin ) VALUES ( %(username)s , %(email)s , %(password)s , NOW() , NOW() , 0 );"
        return connectToMySQL(MyCustomDB).query_db( query, hashed )




    @staticmethod
    def validate_register(data):
        is_valid = True

        query = "SELECT * FROM users WHERE username = %(username)s;"
        results = connectToMySQL(MyCustomDB).query_db(query, data)
        if len(results) >= 1:
            flash("Username has already been taken", "register")
            is_valid = False

        if len(data['username']) < 3:
            flash("Username too Short must be over 3 characters", "register")
            is_valid = False

        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email", "register")
            is_valid = False

        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(MyCustomDB).query_db(query, data)
        if len(results) >= 1:
            flash("email already in use", "register")
            is_valid = False

        if len(data['password']) < 8:
            flash("password needs to be longer than 8", "register")
            is_valid = False

        if data['password'] != data['confirm_password']:
            flash("passwords must match", "register")
            is_valid = False

        return is_valid



    @staticmethod
    def login_submit(data):

        user_in_db = User.get_one_user(data)

        if not user_in_db:
            flash("Invalid Email / Password", "login")
            return False

        if not bcrypt.check_password_hash(user_in_db.password, data["password"]):
            flash("invalid Email/Password", "login")
            return False

        return True

    @classmethod
    def validate_username(cls, data):
        is_valid = True

        query = "SELECT * FROM users WHERE username = %(username)s;"
        results = connectToMySQL(MyCustomDB).query_db(query, data)
        if len(results) >= 1:
            flash("Username has already been taken", "register")
            is_valid = False

        if len(data['username']) < 3:
            flash("Username too Short must be over 3 characters", "register")
            is_valid = False

        return is_valid

    @classmethod
    def profile_update(cls, data):
        query = "UPDATE users SET username = %(username)s, updated_at = NOW() WHERE id = %(id)s"
        return connectToMySQL(MyCustomDB).query_db( query, data )

    @classmethod
    def get_total_written(cls, data):
        query = "SELECT count(*) AS total FROM articles WHERE user_id = %(id)s"
        return connectToMySQL(MyCustomDB).query_db( query, data )