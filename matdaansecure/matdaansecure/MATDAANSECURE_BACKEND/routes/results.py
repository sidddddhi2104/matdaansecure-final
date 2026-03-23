# routes/results.py
from flask import Blueprint, jsonify
from db import query

bp = Blueprint('results', __name__)

@bp.route('/results', methods=['GET'])
def results():
    sql = """
    SELECT c.candidate_id, c.name, c.party, e.title AS election, COUNT(v.vote_id) AS votes
    FROM votes v
    JOIN candidates c ON c.candidate_id = v.candidate_id
    JOIN elections e ON e.election_id = v.election_id
    GROUP BY v.election_id, c.candidate_id
    ORDER BY v.election_id, votes DESC
    """
    rows = query(sql)
    return jsonify({"results": rows})
