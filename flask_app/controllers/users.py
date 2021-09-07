from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import User

@app.route('/')
def index():
    return render_template('index.html')