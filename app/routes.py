from flask import request, jsonify
from app import app
import sqlite3
from app.sms import send_sms_alert
from flask_jwt_extended import jwt_required

DATABASE = 'ecommerce.db'

@app.route('/customers', methods=['POST'])
@jwt_required()
def create_customer():
    data = request.get_json()
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (name, code) VALUES (?, ?)", (data['name'], data['code']))
        conn.commit()
    return jsonify({'message': 'Customer created successfully'}), 201

@app.route('/customers', methods=['GET'])
@jwt_required()
def get_customers():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
    return jsonify(customers), 200

@app.route('/orders', methods=['POST'])
@jwt_required()
def create_order():
    data = request.get_json()
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (customer_id, item, amount, time) VALUES (?, ?, ?, ?)", 
                       (data['customer_id'], data['item'], data['amount'], data['time']))
        conn.commit()

    cursor.execute("SELECT name FROM customers WHERE id=?", (data['customer_id'],))
    customer = cursor.fetchone()
    if customer:
        message = f"Dear {customer[0]}, your order of {data['item']} worth {data['amount']} has been received."
        send_sms_alert(message)

    return jsonify({'message': 'Order created successfully'}), 201

@app.route('/orders', methods=['GET'])
@jwt_required()
def get_orders():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
    return jsonify(orders), 200

@app.route('/')
def index():
    return "E-commerce API is running!"
