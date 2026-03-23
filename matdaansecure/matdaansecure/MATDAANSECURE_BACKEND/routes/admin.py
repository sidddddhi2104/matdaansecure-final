# routes/admin.py
from flask import Blueprint, request, jsonify, make_response
from db import query
from auth import create_jwt, hash_password, check_password, require_jwt

bp = Blueprint('admin', __name__)

@bp.route('/login', methods=['POST'])
def admin_login():
    data = request.json or {}
    username = data.get('username')
    password = data.get('password')
    if not (username and password):
        return jsonify({"error":"missing fields"}), 400
    admin = query("SELECT * FROM admin WHERE username=%s LIMIT 1", (username,), fetchone=True)
    if not admin:
        return jsonify({"error":"invalid credentials"}), 401
    # admin passwords in SQL sample were plain; if hashed, use check_password
    if admin['password'] != password and not check_password(password, admin['password']):
        return jsonify({"error":"invalid credentials"}), 401
    token = create_jwt({"id": admin['admin_id'], "role":"admin", "username":admin['username']})
    resp = make_response(jsonify({"ok":True}))
    resp.set_cookie('matdaan_token', token, httponly=True, samesite='Lax')
    return resp

@bp.route('/corrections', methods=['GET'])
@require_jwt
def list_corrections():
    if request.user.get('role') != 'admin': return jsonify({"error":"forbidden"}), 403
    rows = query("SELECT * FROM corrections WHERE status='pending'")
    return jsonify({"corrections": rows})

@bp.route('/corrections/<int:corr_id>/approve', methods=['POST'])
@require_jwt
def approve(corr_id):
    if request.user.get('role') != 'admin': return jsonify({"error":"forbidden"}), 403
    corr = query("SELECT * FROM corrections WHERE correction_id=%s", (corr_id,), fetchone=True)
    if not corr: return jsonify({"error":"not found"}), 404
    field = corr['field_name']
    # validate allowed fields map
    allowed = {'full_name','email','phone','address','dob'}
    if field not in allowed:
        return jsonify({"error":"invalid field"}), 400
    query(f"UPDATE voters SET {field}=%s WHERE voter_id=%s", (corr['new_value'], corr['voter_id']))
    query("UPDATE corrections SET status='approved' WHERE correction_id=%s", (corr_id,))
    return jsonify({"ok":True, "message":"approved"})
