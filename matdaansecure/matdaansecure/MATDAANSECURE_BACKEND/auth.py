from flask import Blueprint, request, jsonify
from db.connection import get_db
from flask_bcrypt import Bcrypt
import jwt
import datetime
import random
import os

auth = Blueprint("auth", __name__)
bcrypt = Bcrypt()

# Generate JWT
def generate_token(email):
    payload = {
        "email": email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }
    return jwt.encode(payload, os.getenv("JWT_SECRET"), algorithm="HS256")


# -------------------------
# SEND OTP (registration)
# -------------------------
@auth.route("/send-otp", methods=["POST"])
def send_otp():
    data = request.json
    email = data.get("email")

    otp = str(random.randint(100000, 999999))

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO otp_requests (email, otp) VALUES (%s, %s)", (email, otp))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"status": "success", "otp": otp})   # send to frontend to display


# -------------------------
# REGISTER USER
# -------------------------
@auth.route("/register", methods=["POST"])
def register():
    data = request.json
    fullname = data.get("fullname")
    email = data.get("email")
    phone = data.get("phone")
    gender = data.get("gender")
    age = data.get("age")
    voterID = data.get("voterID")
    password = data.get("password")
    user_type = data.get("user_type")  # main, nri, new

    hashed = bcrypt.generate_password_hash(password).decode("utf-8")

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users (fullname, email, phone, gender, age, voterID, password_hash, user_type)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (fullname, email, phone, gender, age, voterID, hashed, user_type))

        conn.commit()
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

    cursor.close()
    conn.close()

    return jsonify({"status": "success", "message": "User registered successfully"})


# -------------------------
# LOGIN USER
# -------------------------
@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE email=%s", (email,))
    row = cursor.fetchone()

    if not row:
        return jsonify({"status": "error", "message": "User not found"}), 404

    stored_hash = row[0]
    if not bcrypt.check_password_hash(stored_hash, password):
        return jsonify({"status": "error", "message": "Incorrect password"}), 401

    token = generate_token(email)

    return jsonify({"status": "success", "token": token})
