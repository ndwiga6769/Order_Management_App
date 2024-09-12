from flask import request, jsonify
from app import app
import sqlite3

# Your routes for customers, orders, and SMS go here

@app.route('/')
def index():
    return "E-commerce API is running!"
