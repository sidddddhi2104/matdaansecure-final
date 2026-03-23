# routes/votes.py
from flask import Blueprint, request, jsonify
from db import query
from auth import require_jwt

bp = Blueprint('votes', __name__)

@bp.route('/candidates', methods=['GET'])
def candidates():
    rows = query("SELECT candidate_id, name, party, symbol FROM candidates")
    return jsonify({"candidates": rows})

@bp.route('/vote', methods=['POST'])
@require_jwt
def vote():
    data = request.json or {}
    candidate_id = data.get('candidate_id')
    election_id = data.get('election_id')
    voter = request.user
    if not (candidate_id and election_id):
        return jsonify({"error":"missing fields"}), 400

    # check if already voted for this election
    existing = query("SELECT * FROM votes WHERE voter_id=%s AND election_id=%s", (voter['id'], election_id), fetchone=True)
    if existing:
        return jsonify({"error":"already voted"}), 403
    try:
        query("INSERT INTO votes (voter_id, candidate_id, election_id) VALUES (%s,%s,%s)",
              (voter['id'], candidate_id, election_id))
        return jsonify({"ok":True, "message":"vote recorded"})
    except Exception as e:
        return jsonify({"error":"db error", "details": str(e)}), 500
