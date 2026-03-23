# routes/notifications.py
from flask import Blueprint, request, jsonify
from auth import require_jwt
import os, json
from firebase_admin import credentials, initialize_app, messaging

bp = Blueprint('notifications', __name__)

# initialize firebase admin once
if os.path.exists(os.getenv('FIREBASE_SERVICE_ACCOUNT_JSON') or 'serviceAccount.json'):
    cred = credentials.Certificate(os.getenv('FIREBASE_SERVICE_ACCOUNT_JSON') or 'serviceAccount.json')
    try:
        initialize_app(cred)
    except Exception:
        pass

@bp.route('/send', methods=['POST'])
@require_jwt
def send():
    if request.user.get('role') != 'admin': return jsonify({"error":"forbidden"}), 403
    data = request.json or {}
    token = data.get('fcm_token')
    title = data.get('title')
    body = data.get('body')
    if not (token and title):
        return jsonify({"error":"missing fields"}), 400
    message = messaging.Message(
        token=token,
        notification=messaging.Notification(title=title, body=body),
        data=data.get('data') or {}
    )
    try:
        res = messaging.send(message)
        return jsonify({"ok":True, "message_id": res})
    except Exception as e:
        return jsonify({"error":"fcm failed", "details": str(e)}), 500
