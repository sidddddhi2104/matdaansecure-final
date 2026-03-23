# routes/public.py
from flask import Blueprint, request, jsonify, make_response
from db import query
from auth import hash_password, check_password, create_jwt

bp = Blueprint('public', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.json or {}
    name = data.get('full_name')
    email = data.get('email')
    phone = data.get('phone')
    dob = data.get('dob')
    password = data.get('password')
    if not (name and email and password and dob and phone):
        return jsonify({"error":"missing fields"}), 400

    hashed = hash_password(password)
    try:
        sql = "INSERT INTO voters (full_name,email,phone,dob,password) VALUES (%s,%s,%s,%s,%s)"
        query(sql, (name,email,phone,dob,hashed))
        return jsonify({"ok":True, "message":"registered"}), 201
    except Exception as e:
        return jsonify({"error":"db error", "details": str(e)}), 500

@bp.route('/login', methods=['POST'])
def login():
    data = request.json or {}
    email = data.get('email')
    password = data.get('password')
    if not (email and password):
        return jsonify({"error":"missing fields"}), 400
    user = query("SELECT * FROM voters WHERE email=%s LIMIT 1", (email,), fetchone=True)
    if not user or not check_password(password, user['password']):
        return jsonify({"error":"invalid credentials"}), 401
    payload = {"id": user['voter_id'], "role":"voter", "email":user['email']}
    token = create_jwt(payload)
    resp = make_response(jsonify({"ok":True, "voter_id": user['voter_id']}))
    resp.set_cookie('matdaan_token', token, httponly=True, samesite='Lax')  # secure=True in prod
    return resp
