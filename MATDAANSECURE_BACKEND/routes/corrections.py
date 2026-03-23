# routes/corrections.py
from flask import Blueprint, request, jsonify
from db import query
from auth import require_jwt

bp = Blueprint('corrections', __name__)

@bp.route('/corrections', methods=['POST'])
@require_jwt
def submit():
    data = request.json or {}
    field = data.get('field_name')
    new_value = data.get('new_value')
    if not (field and new_value):
        return jsonify({"error":"missing fields"}), 400
    # fetch old
    cur = query(f"SELECT {field} FROM voters WHERE voter_id=%s", (request.user['id'],), fetchone=True)
    old = cur.get(field) if cur else None
    query("INSERT INTO corrections (voter_id, field_name, old_value, new_value) VALUES (%s,%s,%s,%s)",
          (request.user['id'], field, old, new_value))
    return jsonify({"ok":True, "message":"submitted"})
