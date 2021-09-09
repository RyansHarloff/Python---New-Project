from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['first_name']) < 2:
            flash("First Name must be longer than 2 characters")
            is_valid = False
        if len(data["last_name"]) < 2:
            flash("Last Name must be longer than 2 characters")
            is_valid = False
        if not EMAIL_REGEX.match(data["email"]):
            flash("Not a valid email address")
            is_valid = False
        if len(data["password"]) < 8:
            flash("Password must be at least 8 characters")
            is_valid = False
        if not data["password"] == data["conf_password"]:
            flash("Password and Confirmation Password must Match")
            is_valid = False
        return is_valid

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW());"
        return connectToMySQL("python-cars").query_db(query,data)