from flask import Flask, request, jsonify, session, send_from_directory
from flask_cors import CORS
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import face_recognition
from datetime import datetime, timedelta
import os
import pickle
from flask import Flask, jsonify, request
import cv2
import numpy as np
import io
import uuid
import random
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_cors import CORS
import cv2
import numpy as np
import mysql.connector
import base64  # Add this at the top of app.py 
import face_recognition
import firebase_admin
from firebase_admin import credentials, messaging
from flask import request
from flask import send_file, session
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import lightgrey
from reportlab.lib.units import cm
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from datetime import datetime
import uuid
import os
from reportlab.platypus import Image
from reportlab.lib.utils import ImageReader
from PIL import Image as PILImage, ImageDraw, ImageFont
import tempfile
import os
import uuid
from datetime import datetime

from flask import send_file, session
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    Frame, PageTemplate, Image
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing



app = Flask(__name__)
app.secret_key = "matdaansecure_secret"

# 🔥 Firebase Admin Initialization (DO THIS ONLY ONCE)
cred = credentials.Certificate("matdaan-d1486-firebase-adminsdk-fbsvc-3e4c4b226d.json")
firebase_admin.initialize_app(cred)
# =============================================================
# BASIC CONFIG
# =============================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Your HTML files are one level ABOVE MATDAANSECURE_BACKEND
FRONTEND_DIR = os.path.abspath(
    os.path.join(BASE_DIR, "..")
)

print("FRONTEND_DIR =", FRONTEND_DIR)
CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True
)

# =====================================================
# ================= PAGE ROUTES =======================
# =====================================================

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/admin-analytics")
def admin_analytics():
    return render_template("admin-analytics.html")

@app.route("/admin-dashboard")
def admin_dashboard():
    return render_template("admin-dashboard.html")

@app.route("/admin-election-settings")
def admin_election_settings():
    return render_template("admin-election-settings.html")

@app.route("/admin-feedback")
def admin_feedback():
    return render_template("admin-feedback.html")

@app.route("/admin-logs")
def admin_logs():
    return render_template("admin-logs.html")

@app.route("/admin-manage-candidates")
def admin_manage_candidates():
    return render_template("admin-manage-candidates.html")

@app.route("/admin-manage-voters")
def admin_manage_voters():
    return render_template("admin-manage-voters.html")

@app.route('/candidate/<candidate_code>')
def candidate_page(candidate_code):
    try:
        return render_template(f"candidate-{candidate_code}.html")
    except:
        return "Candidate page not found", 404

@app.route("/candidate-C001")
def candidate_C001():
    return render_template("candidate-C001.html")

@app.route("/candidate-C002")
def candidate_C002():
    return render_template("candidate-C002.html")

@app.route("/candidate-C003")
def candidate_C003():
    return render_template("candidate-C003.html")

@app.route("/candidate-C004")
def candidate_C004():
    return render_template("candidate-C004.html")

@app.route("/candidate-C005")
def candidate_C005():
    return render_template("candidate-C005.html")

@app.route("/candidate-C006")
def candidate_C006():
    return render_template("candidate-C006.html")

@app.route("/candidate-C007")
def candidate_C007():
    return render_template("candidate-C007.html")

@app.route("/candidate-C008")
def candidate_C008():
    return render_template("candidate-C008.html")

@app.route("/candidate-C009")
def candidate_C009():
    return render_template("candidate-C009.html")

@app.route("/candidate-C010")
def candidate_C010():
    return render_template("candidate-C010.html")

@app.route("/candidate-C011")
def candidate_C011():
    return render_template("candidate-C011.html")

@app.route('/candidates')
def candidates_page():
    return render_template('candidates.html')

@app.route("/change-password.html")
def change_password():
    return render_template("change-password.html")

@app.route("/complaints")
def complaints():
    return render_template("complaints.html")

@app.route("/correction")
def correction_page():
    return render_template("correction.html")

@app.route("/delete-account.html")
def delete_account():
    return render_template("delete-account.html")
    
@app.route('/favicon.ico')
def favicon():
    return '', 204


@app.route("/elector-roll.html")
def elector_roll():
    return render_template("elector-roll.html")

@app.route("/face_register")
@app.route("/face-register")
def face_register_page():
    return render_template("face_register.html")

@app.route('/face-verify')
@app.route('/face_verify')
def face_verify():
    return render_template('face-verify.html')

@app.route("/face-update")
def face_update_page():
    return render_template("face_update.html")

@app.route("/firebase-messaging-sw.js")
def service_worker():
    return send_from_directory(
        directory=app.static_folder,
        path="firebase-messaging-sw.js",
        mimetype="application/javascript"
    )

@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/mystatus.html")
def mystatus():
    return render_template("mystatus.html")

@app.route("/notifications.html")
def notifications():
    return render_template("notifications.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/reset-password.html")
def reset_password_page():
    return render_template("reset-password.html")

@app.route("/result.html")
def result():
    return render_template("result.html")

@app.route("/start.html")
def start():
    return render_template("start.html")

@app.route("/suggestion.html")
def suggestion():
    return render_template("suggestion.html")

@app.route("/thankyou.html")
def thankyou():
    return render_template("thankyou.html")

@app.route("/vote.html")
def vote():
    return render_template("vote.html")


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'matdaansecure'
}


def get_db_connection():
    """Establishes a connection to the MySQL database."""
    return mysql.connector.connect(**db_config)

def get_cursor():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    return conn, cursor

def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)

def decode_image(data):
    img = base64.b64decode(data.split(",")[1])
    npimg = np.frombuffer(img, np.uint8)
    return cv2.imdecode(npimg, cv2.IMREAD_COLOR)

def texture_score(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    return lap.var()

def add_log(voterID, fullname, activity):
    print("📝 LOG TRY:", voterID, fullname, activity)  # 👈 DEBUG LINE

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO logs (voterID, fullname, activity)
            VALUES (%s, %s, %s)
        """, (voterID, fullname, activity))

        conn.commit()
        cursor.close()
        conn.close()

        print("✅ LOG INSERTED")

    except Exception as e:
        print("❌ LOG INSERT ERROR:", e)

def normalize_photo(photo):
    if not photo:
        return "NOTA.jpeg"
    return photo.split("\\")[-1].split("/")[-1]


def motion_score(img1, img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(gray1, gray2)
    return np.mean(diff)

def format_row(row):
    return {
        "reference_id": row.get("reference_id"),
        "voter_id": row.get("voter_id"),
        "feedback_type": row.get("feedback_type"),
        "field_name": row.get("field_name"),
        "old_value": row.get("old_value"),
        "new_value": row.get("new_value"),
        "message": row.get("message"),
        "status": row.get("status"),
        "created_at": row.get("created_at").strftime("%d %b %Y")
    }

def is_value_blocked(cursor, field_name, value):
    # 1️⃣ Current users
    cursor.execute(
        f"SELECT 1 FROM users WHERE {field_name} = %s LIMIT 1",
        (value,)
    )
    if cursor.fetchone():
        return True

    # 2️⃣ Old approved corrections
    cursor.execute("""
        SELECT 1 FROM corrections
        WHERE field_name = %s
          AND old_value = %s
          AND status = 'APPROVED'
        LIMIT 1
    """, (field_name, value))

    return cursor.fetchone() is not None

def send_push(token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        token=token
    )
    messaging.send(message)

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import cm


def generate_vote_pdf(voter_id, candidate_name, vote_id, output_path):
    """
    Generates official MATDAANSECURE voting receipt PDF
    """

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm
    )

    story = []

    # ---- HEADER ----
    story.append(Paragraph("<b>MATDAANSECURE</b>", styles["Title"]))
    story.append(Paragraph("Official Voting Receipt", styles["Heading2"]))
    story.append(Spacer(1, 20))

    # ---- TABLE DATA ----
    data = [
        ["Voter ID", voter_id],
        ["Candidate ID", candidate_name],
        ["Vote Proof ID", vote_id],
        ["Status", "VOTED ✔"],
    ]

    table = Table(data, colWidths=[6 * cm, 8 * cm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.whitesmoke),
        ("GRID", (0, 0), (-1, -1), 1, colors.grey),
        ("FONT", (0, 0), (-1, -1), "Helvetica"),
        ("FONT", (0, 0), (0, -1), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
    ]))

    story.append(table)
    story.append(Spacer(1, 30))

    # ---- FOOTER ----
    story.append(Paragraph(
        "This document serves as an official proof that your vote has been securely recorded.",
        styles["Normal"]
    ))

    doc.build(story)

def normalize_phone(phone):
    if not phone:
        return None
    phone = phone.strip().replace(" ", "")
    if phone.startswith("+91"):
        phone = phone[3:]
    return phone

import qrcode
import os

def generate_voter_qr(voter_id, name, phone):
    qr_folder = os.path.join(app.root_path, "static", "qr")
    os.makedirs(qr_folder, exist_ok=True)

    qr_filename = f"{voter_id}.png"
    qr_path = os.path.join(qr_folder, qr_filename)

    # Generate only if not exists
    if not os.path.exists(qr_path):
        qr_data = f"VOTER ID: {voter_id}\nNAME: {name}\nPHONE: {phone}"
        qr = qrcode.make(qr_data)
        qr.save(qr_path)

    return f"qr/{qr_filename}"


# =============================================================
# ---------------------- USER REGISTRATION --------------------
# =============================================================
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        if not data:
            return jsonify(status="error", message="No JSON data received"), 400

        # ----------- CLEAN INPUTS -----------
        fullname = (data.get('fullname') or '').strip()
        email = (data.get('email') or '').strip()
        phone = normalize_phone(data.get('phone'))
        gender = (data.get('gender') or '').strip()
        age = data.get('age')
        voterID = (data.get('voterID') or '').strip()
        password = (data.get('password') or '').strip()
        user_type = (data.get('type') or 'new').strip()

        parent_name = (data.get('parent_name') or '').strip() or None
        passport = (data.get('passport') or '').strip() or None
        dob = (data.get('dob') or '').strip() or None
        address = (data.get('address') or '').strip() or None

        # ----------- BASIC VALIDATION -----------
        if not all([fullname, email, phone, voterID, password]):
            return jsonify(status="error", message="Missing required fields"), 400

        if age is not None:
            try:
                age = int(age)
            except ValueError:
                return jsonify(status="error", message="Invalid age"), 400

        hashed_pw = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            # 🔐 GLOBAL BLOCK CHECK (CURRENT + OLD CORRECTED VALUES)
            fields_to_check = {
                "email": email,
                "phone": phone,
                "voterID": voterID
            }

            for field, value in fields_to_check.items():
                if is_value_blocked(cursor, field, value):
                    return jsonify(
                        status="exists",
                        message=f"{field} has already been used earlier"
                    ), 409

            # ✅ INSERT USER
            cursor.execute("""
                INSERT INTO users
                (fullname, email, phone, gender, age, voterID, password_hash,
                 user_type, parent_name, passport, dob, address, created_at)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                fullname,
                email,
                phone,
                gender,
                age,
                voterID,
                hashed_pw,
                user_type,
                parent_name,
                passport,
                dob,
                address,
                datetime.now()
            ))

            conn.commit()

        except Exception as db_err:
            conn.rollback()

            if "Duplicate entry" in str(db_err):
                return jsonify(
                    status="exists",
                    message="You have already registered. Please login."
                ), 409

            raise db_err

        finally:
            cursor.close()
            conn.close()

        add_log(voterID, fullname, "User Registered")

        return jsonify(
            status="success",
            message="Registration Successful"
        ), 200

    except Exception as e:
        print("Registration Error:", e)
        return jsonify(status="error", message=str(e)), 500

# =============================================================
# ---------------------- LOGIN  ------------------------
# =============================================================
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    phone = data.get('phone')
    password = data.get('password')

    if not phone or not password:
        return jsonify({"error": "Phone & Password required"}), 400
        # ✅ BUILT-IN ADMIN LOGIN
    if phone == "admin" and password == "admin123":
        session.clear()
        session["admin_logged_in"] = True
        session.permanent = True
        return jsonify({
            "status": "admin_login",
            "redirect": "/admin-dashboard"
        }), 200

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, phone, password_hash FROM users WHERE phone=%s", (phone,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    # ❌ USER NOT FOUND
    if not user:
        add_log("UNKNOWN", "UNKNOWN", f"Login Failed (phone={phone})")
        return jsonify({"error": "User not found"}), 404

    # ❌ WRONG PASSWORD
    if not check_password_hash(user["password_hash"], password):
        add_log("UNKNOWN", "UNKNOWN", "Wrong Password")
        return jsonify({"error": "Invalid password"}), 401

    # ✅ PASSWORD VERIFIED → ALLOW OTP STEP
    session.clear()
    session["pre_auth_phone"] = phone   # 🔐 temp auth
    session.permanent = True

    return jsonify({
        "status": "password_ok",
        "message": "Password verified. Proceed to OTP."
    }), 200
# =============================================================
# ---------------------- CHECK USER --------------------
# =============================================================
@app.route('/check-user', methods=['POST'])
def check_user():
    try:
        data = request.json or {}

        email = (data.get("email") or "").strip()
        phone = (data.get("phone") or "").strip()
        voterID = (data.get("voterID") or "").strip()

        if not any([email, phone, voterID]):
            return jsonify(
                status="error",
                message="At least one identifier required"
            ), 400

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT voterID, email, phone
            FROM users
            WHERE email = %s
               OR phone = %s
               OR voterID = %s
            LIMIT 1
        """, (email, phone, voterID))

        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            return jsonify({
                "status": "exists",
                "matched_on": {
                    "email": user["email"] == email,
                    "phone": user["phone"] == phone,
                    "voterID": user["voterID"] == voterID
                }
            }), 409

        return jsonify(status="not_exists"), 200

    except Exception as e:
        print("CHECK USER ERROR:", e)
        return jsonify(status="error", message="Server error"), 500


# =============================================================
# ---------------------- RESET PASSWORD --------------------
# =============================================================
@app.route('/reset_password', methods=['POST'])
def reset_password():
    email = request.form.get('email')
    new_password = request.form.get('password')

    if not email or not new_password:
        return jsonify({"status": "error", "message": "Missing data"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Fetch the current password hash for this email
    cursor.execute("SELECT password_hash FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()

    if not user:
        cursor.close()
        conn.close()
        return jsonify({"status": "error", "message": "Email not found"}), 404

    current_hashed_password = user[0]

    # 2. Check if the new password is the same as the old one
    if check_password_hash(current_hashed_password, new_password):
        cursor.close()
        conn.close()
        return jsonify({
            "status": "error", 
            "message": "New password cannot be the same as your current password."
        }), 400

    # 3. If it's a new password, hash it and update
    new_hashed_password = generate_password_hash(new_password)
    cursor.execute(
        "UPDATE users SET password_hash=%s WHERE email=%s",
        (new_hashed_password, email)
    )
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "status": "success",
        "message": "Password updated successfully"
    })
# =============================================================
# ---------------------- SAVE ELECTION SETTINGS --------------------
# =============================================================
@app.route('/save_election_settings', methods=['POST'])
def save_election_settings():
    data = request.json

    title = data.get('title')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    status = data.get('status')

    if not title or not start_date or not end_date:
        return jsonify({'error': 'Missing fields (title, start_date, end_date)'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO elections (title, start_date, end_date, status)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (title, start_date, end_date, status))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': 'Election settings saved successfully'})

    except Exception as e:
        print(f"Error saving election settings: {e}")
        return jsonify({'error': str(e)}), 500

# =============================================================
# ---------------------- GET ELECTION SETTINGS --------------------
# =============================================================
@app.route('/get_election_settings', methods=['GET'])
def get_election_settings():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT election_id, title, start_date, end_date, status, result_published
            FROM elections ORDER BY election_id DESC LIMIT 1
        """)

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if not row:
            return jsonify({'error': 'No election found'}), 404

        return jsonify({
            "election_id": row["election_id"],
            "title": row["title"],
            "start_date": str(row["start_date"]),
            "end_date": str(row["end_date"]),
            "status": row["status"],
            "result_published": row["result_published"]  # 🔥 add this
        })

    except Exception as e:
        print(f"Error retrieving election settings: {e}")
        return jsonify({'error': str(e)}), 500
# =============================================================
# ---------------------- ADD ELECTION --------------------
# =============================================================
@app.route('/add_election', methods=['POST'])
def add_election():
    try:
        data = request.json

        title = data['title']
        start_date = data['start_date']
        end_date = data['end_date']
        status = "not_started"

        if not title or not start_date or not end_date:
            return jsonify({'error': 'Missing title, start_date, or end_date'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("UPDATE elections SET status='ended' WHERE status!='ended'")

        cursor.execute("""
            INSERT INTO elections (title, start_date, end_date, status)
            VALUES (%s, %s, %s, %s)
        """, (title, start_date, end_date, status))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({
            "success": True,
            "message": "New election scheduled. Previous elections have been marked as ended."
        })

    except Exception as e:
        print(f"Error adding new election: {e}")
        return jsonify({"error": str(e)}), 500

# =============================================================
# ---------------------- ADMIN LOGIN --------------------
# =============================================================
@app.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.json

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"status": False, "message": "Username and password required"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT admin_id, username, password FROM admin WHERE username = %s",
            (username,)
        )

        admin = cursor.fetchone()

        cursor.close()
        conn.close()

        if not admin:
            return jsonify({"status": False, "message": "Admin not found"}), 401

        if check_password_hash(admin['password'], password):
            return jsonify({
                "status": True,
                "message": "Admin Login Success",
                "admin_id": admin['admin_id'],
                "username": admin['username']
            }), 200

        return jsonify({"status": False, "message": "Incorrect Password"}), 401

    except Exception as e:
        print("Admin login error:", e)
        return jsonify({"status": False, "message": "Server Error"}), 500

# =============================================================
# ---------------------- ADMIN RESULT PUBLISHMENT --------------------
# =============================================================
@app.route('/publish_result', methods=['POST'])
def publish_result():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Get latest election
        cursor.execute("SELECT election_id FROM elections ORDER BY election_id DESC LIMIT 1")
        latest = cursor.fetchone()

        if not latest:
            return jsonify({"error": "No election found"}), 404

        election_id = latest[0]

        cursor.execute("""
    UPDATE elections 
    SET result_published = 1, status='result_published'
    WHERE election_id = %s
""", (election_id,))

        cursor.execute("UPDATE voters SET notified_result = 1")

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Result Published Successfully!"})

    except Exception as e:
        print("Publish result error:", e)
        return jsonify({"error": "Server error"}), 500

# =============================================================
# ---------------------- RESULT STATUS --------------------
# =============================================================
@app.route('/result_status', methods=['GET'])
def result_status():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT election_id, result_published 
            FROM elections 
            ORDER BY election_id DESC LIMIT 1
        """)
        
        status = cursor.fetchone()

        cursor.close()
        conn.close()

        if not status:
            return jsonify({"error": "No election found"}), 404

        return jsonify(status)

    except Exception as e:
        print("Result status error:", e)
        return jsonify({"error": str(e)}), 500
# =============================================================
# ---------------------- GET ACTIVE CANDIDATES ----------------
# =============================================================
@app.route("/get-candidates")
def get_candidates_with_photos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM candidates")
    candidates = cursor.fetchall()

    for c in candidates:
        if c["photo"]:
            c["photo"] = "/static/images/" + c["photo"].split("\\")[-1]

    cursor.close()
    conn.close()

    return jsonify(candidates=candidates)

# =============================================================
# ---------------------- GET CANDIDATES(VOTERS)--------------------
# =============================================================
@app.route("/api/candidates", methods=["GET"])
def api_candidates():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, name, party, photo, symbol
        FROM candidates
        WHERE status = 'Active'
    """)
    rows = cursor.fetchall()

    for r in rows:
        r["photo"] = normalize_photo(r["photo"])

    cursor.close()
    conn.close()

    return jsonify(rows)

# =============================================================
# ---------------------- GET CANDIDATES(ADMIN)--------------------
# =============================================================
@app.route("/get-candidates", methods=["GET"])
def get_candidates():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM candidates")
    rows = cursor.fetchall()

    for r in rows:
        r["photo"] = normalize_photo(r["photo"])

    cursor.close()
    conn.close()

    return jsonify(candidates=rows)
# =============================================================
# ---------------------- ADD CANDIDATES--------------------
# =============================================================
@app.route("/add-candidate", methods=["POST"])
def add_candidate():
    data = request.get_json()

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # 1. First, reset the auto_increment to ensure no gaps (e.g. jumping to 26)
        cursor.execute("ALTER TABLE candidates AUTO_INCREMENT = 1")

        # 2. Insert ALL fields including age, education, experience, and candidate_code
        cursor.execute("""
            INSERT INTO candidates 
            (name, age, education, experience, party, photo, symbol, status, candidate_code)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            data["name"],
            data.get("age"),             # Uses .get() in case field is empty
            data.get("education"),
            data.get("experience"),
            data["party"],
            normalize_photo(data["photo"]),
            data["symbol"],
            data["status"],
            data.get("candidate_code")   # This saves the "C011" generated by frontend
        ))

        conn.commit()
        return jsonify(success=True)
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify(success=False, error=str(e)), 500
    
    finally:
        cursor.close()
        conn.close()
# =============================================================
# ---------------------- UPDATE CANDIDATES --------------------
# =============================================================
@app.route("/update-candidate/<int:id>", methods=["PUT"])
def update_candidate(id):
    data = request.get_json()

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE candidates
        SET name=%s, party=%s, photo=%s, symbol=%s, status=%s
        WHERE id=%s
    """, (
        data["name"],
        data["party"],
        normalize_photo(data["photo"]),
        data["symbol"],
        data["status"],
        id
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify(success=True)
# =============================================================
# ---------------------- DELETE CANDIDATES --------------------
# =============================================================
@app.route("/delete-candidate/<int:id>", methods=["DELETE"])
def delete_candidate(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM candidates WHERE id=%s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify(success=True)
# =============================================================
# ---------------------- SUBMIT VOTE --------------------
# =============================================================
@app.route("/submit-vote", methods=["POST"])
def submit_vote():

    if "voter_id" not in session:
        return jsonify({"error": "Session expired. Please login again."}), 401

    voter_id = session["voter_id"]

    data = request.get_json()
    raw_candidate = data.get("candidate_id")

    if not raw_candidate:
        return jsonify({"error": "Missing candidate"}), 400

    # Normalize candidate ID
    if str(raw_candidate).isdigit():
        candidate_id = f"C{int(raw_candidate):03d}"
    else:
        candidate_id = str(raw_candidate).strip().upper()

    # Store temporary (will be replaced after DB fetch)
    session["candidate_name"] = candidate_id

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # ❌ Prevent double voting
        cursor.execute(
            "SELECT 1 FROM votes WHERE voter_id = %s",
            (voter_id,)
        )
        if cursor.fetchone():
            return jsonify({"error": "You already voted"}), 403

        # ✅ Generate UNIQUE vote proof ID (ONCE)
        vote_proof_id = "VOTE-" + uuid.uuid4().hex[:10].upper()

        # ✅ Insert vote (ONLY ONCE)
        cursor.execute("""
            INSERT INTO votes (voter_id, candidate_id, vote_proof_id, voted_at)
            VALUES (%s, %s, %s, NOW())
        """, (voter_id, candidate_id, vote_proof_id))

        # ✅ Update vote count
        cursor.execute("""
            INSERT INTO candidate_votes (candidate_id, total_votes)
            VALUES (%s, 1)
            ON DUPLICATE KEY UPDATE total_votes = total_votes + 1
        """, (candidate_id,))

        conn.commit()

        # ✅ Fetch candidate name safely (DO NOT BREAK VOTE)
        try:
            cursor.execute(
                "SELECT name FROM candidates WHERE candidate_id = %s",
                (candidate_id,)
            )
            row = cursor.fetchone()
            session["candidate_name"] = row[0] if row else candidate_id

        except Exception as e:
            print("CANDIDATE NAME FETCH ERROR:", e)
            session["candidate_name"] = candidate_id


        add_log(voter_id, "Voter", f"Voted for {candidate_id}")

        return jsonify({
            "message": "Vote submitted successfully",
            "vote_proof_id": vote_proof_id
        }), 200

    except Exception as e:
        conn.rollback()
        print("VOTE ERROR:", e)
        return jsonify({"error": "Server error"}), 500

    finally:
        cursor.close()
        conn.close()


# =============================================================
# ---------------------- VOTE COUNTS --------------------
# =============================================================
@app.route("/vote-counts", methods=["GET"])
def vote_counts():
    try:
        conn = get_db_connection()
        cur = conn.cursor(dictionary=True)

        cur.execute("SELECT candidate_id, COUNT(*) AS votes FROM votes GROUP BY candidate_id")
        rows = cur.fetchall()

        cur.close()
        conn.close()

        return jsonify({"status": "success", "counts": rows})
    except Exception as e:
        print("Vote count error:", e)
        return jsonify({"status": "error", "message": str(e)}), 500#
# =============================================================
# ---------------------- ADMIN APPROVE CORRECTION --------------------
# =============================================================
@app.route("/admin/approve_correction", methods=["POST"])
def approve_correction():
    try:
        data = request.get_json()
        reference_id = data.get("reference_id")

        if not reference_id:
            return jsonify(success=False, message="Reference ID missing"), 400

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT voter_id, field_name, new_value
            FROM corrections
            WHERE reference_id = %s
              AND status = 'PENDING'
        """, (reference_id,))

        correction = cursor.fetchone()
        if not correction:
            return jsonify(success=False, message="No pending correction"), 404

        voter_id = correction["voter_id"]
        field_name = correction["field_name"]
        new_value = correction["new_value"]

        # 🔐 Prevent duplicate values
        cursor.execute(
            f"SELECT id FROM users WHERE {field_name} = %s AND voterID != %s",
            (new_value, voter_id)
        )
        if cursor.fetchone():
            return jsonify(
                success=False,
                message="New value already used by another user"
            ), 409

        # ✅ Update users
        cursor.execute(
            f"UPDATE users SET {field_name} = %s WHERE voterID = %s",
            (new_value, voter_id)
        )

        # ✅ Mark correction approved
        cursor.execute("""
            UPDATE corrections
            SET status = 'APPROVED'
            WHERE reference_id = %s
        """, (reference_id,))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify(success=True, message="Correction approved")

    except Exception as e:
        print("APPROVE ERROR:", e)
        return jsonify(success=False, message=str(e)), 500

# =============================================================
# ---------------------- UPLOADS----------------
# =============================================================
from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

# =============================================================
# ---------------------- VIEW DOCUMENT----------------
# =============================================================
@app.route("/view-document/<filename>")
def view_document(filename):
    return render_template("document-viewer.html", filename=filename)
# =============================================================
# ---------------------- USER SUBMIT CORRECTION ----------------
# =============================================================
from flask import request, jsonify
import uuid
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/submit-correction", methods=["POST"])
def submit_correction():
    try:
        # ✅ RECEIVE FORM DATA (FormData from frontend)
        voter_id   = request.form.get("voter_id")
        field_name = request.form.get("field_name")
        new_value  = request.form.get("new_value")

        # ✅ RECEIVE FILE
        file = request.files.get("document")

        if not voter_id or not field_name or not new_value:
            return jsonify(
                success=False,
                message="Missing required fields"
            ), 400

        # 🔐 ALLOWED FIELDS (SECURITY WHITELIST)
        allowed_fields = {
            "fullname",
            "email",
            "phone",
            "gender",
            "age",
            "parent_name",
            "passport",
            "dob",
            "address"
        }

        if field_name not in allowed_fields:
            return jsonify(
                success=False,
                message="Invalid correction field"
            ), 400

        reference_id = "CORR-" + uuid.uuid4().hex[:6].upper()

        conn = get_db_connection()
        cursor = conn.cursor()

        # ✅ FETCH OLD VALUE SAFELY
        query = f"SELECT `{field_name}` FROM users WHERE voterID = %s"
        cursor.execute(query, (voter_id,))
        result = cursor.fetchone()

        if not result:
            cursor.close()
            conn.close()
            return jsonify(
                success=False,
                message="User not found"
            ), 404

        old_value = result[0]

        # 🛑 PREVENT SAME VALUE CORRECTION
        if old_value is not None and str(old_value).strip() == str(new_value).strip():
            cursor.close()
            conn.close()
            return jsonify(
                success=False,
                message="New value must be different from old value"
            ), 400

        # ✅ SAVE DOCUMENT IF PROVIDED
        filename = None
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)

        # ✅ INSERT CORRECTION REQUEST
        cursor.execute("""
            INSERT INTO corrections
            (reference_id, voter_id, field_name, old_value, new_value, document, status)
            VALUES (%s, %s, %s, %s, %s, %s, 'PENDING')
        """, (
            reference_id,
            voter_id,
            field_name,
            old_value,
            new_value,
            filename
        ))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify(
            success=True,
            reference_code=reference_id
        ), 200

    except Exception as e:
        print("❌ SUBMIT CORRECTION ERROR:", e)
        return jsonify(
            success=False,
            message=str(e)
        ), 500
# =============================================================
# ---------------------- USER SUBMIT COMPLAINT -----------------
# =============================================================
from flask import request, jsonify
from datetime import datetime
import random

@app.route("/submit_complaint", methods=["POST"])
def submit_complaint():
    try:
        data = request.get_json()
        print("📥 Complaint Data:", data)

        if not data:
            return jsonify(success=False, error="No data received"), 400

        voter_id = data.get("voter_id")
        complaint_type = data.get("complaint_type")
        complaint_text = data.get("complaint")

        if not voter_id or not complaint_type or not complaint_text:
            return jsonify(
                success=False,
                error="Missing required fields"
            ), 400

        reference_id = f"COMP-{datetime.now().year}-{random.randint(100000, 999999)}"

        conn = get_db_connection()
        cursor = conn.cursor()

        # ✅ RENAMED `type` → `complaint_type`
        cursor.execute("""
            INSERT INTO complaints
            (reference_id, voter_id, complaint_type, message, status)
            VALUES (%s, %s, %s, %s, 'PENDING')
        """, (
            reference_id,
            voter_id,
            complaint_type,
            complaint_text
        ))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify(
            success=True,
            reference_code=reference_id
        ), 200

    except Exception as e:
        print("❌ Complaint Error:", e)
        return jsonify(success=False, error=str(e)), 500
# =============================================================
# ---------------------- USER SUBMIT SUGGESTION --------------------
# =============================================================
@app.route("/submit_suggestion", methods=["POST"])
def submit_suggestion():
    try:
        data = request.get_json()
        if not data:
            return jsonify(success=False, message="No JSON received"), 400

        voter_id = data.get("voter_id")
        suggestion_type = data.get("type", "GENERAL")
        message = data.get("message")

        if not voter_id or not message:
            return jsonify(success=False, message="Missing fields"), 400

        reference_id = "SUG-" + uuid.uuid4().hex[:8].upper()

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO suggestions
            (reference_id, voter_id, type, message, status)
            VALUES (%s, %s, %s, %s, 'PENDING')
        """, (
            reference_id,
            voter_id,
            suggestion_type,
            message
        ))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify(
            success=True,
            reference_code=reference_id
        ), 200

    except Exception as e:
        print("❌ SUBMIT SUGGESTION ERROR:", e)
        return jsonify(success=False, message=str(e)), 500

# =============================================================
# ---------------------- ADMIN GET COMPLAINTS --------------------
# =============================================================
@app.route("/admin/get_complaints")
def get_complaints():
    conn = mysql.connector.connect(
        host="localhost", user="root", password="", database="matdaansecure"
    )
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM complaints ORDER BY created_at DESC")
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return jsonify(data)

# =============================================================
# ---------------------- ADMIN APPROVE COMPLAINTS --------------------
# =============================================================
@app.route("/admin/approve_complaint", methods=["POST"])
def approve_complaint():
    data = request.get_json()
    reference_id = data.get("reference_id")

    if not reference_id:
        return jsonify(success=False), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE complaints
        SET status='APPROVED'
        WHERE reference_id=%s
          AND status='PENDING'
    """, (reference_id,))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify(success=True)
# =============================================================
# ---------------------- ADMIN REJECT COMPLAINTS --------------------
# =============================================================
@app.route("/admin/reject_complaint", methods=["POST"])
def reject_complaint():
    data = request.get_json()
    reference_id = data.get("reference_id")

    if not reference_id:
        return jsonify(success=False), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE complaints
        SET status='REJECTED'
        WHERE reference_id=%s
          AND status='PENDING'
    """, (reference_id,))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify(success=True)
# =============================================================
# ---------------------- ADMIN GET SUGGESTIONS --------------------
# =============================================================
@app.route("/admin/get_suggestions")
def get_suggestions():
    conn = mysql.connector.connect(
        host="localhost", user="root", password="", database="matdaansecure"
    )
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM suggestions ORDER BY created_at DESC")
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return jsonify(data)

# =============================================================
# ---------------------- ADMIN APPROVE SUGGESTION -----------------
# =============================================================
@app.route("/admin/approve_suggestion", methods=["POST"])
def approve_suggestion():
    data = request.get_json()
    reference_id = data.get("reference_id")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE suggestions
        SET status='APPROVED'
        WHERE reference_id=%s
          AND status='PENDING'
    """, (reference_id,))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify(success=True)
# =============================================================
# ---------------------- ADMIN REJECT SUGGESTION -----------------
# =============================================================
@app.route("/admin/reject_suggestion", methods=["POST"])
def reject_suggestion():
    data = request.get_json()
    reference_id = data.get("reference_id")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE suggestions
        SET status='REJECTED'
        WHERE reference_id=%s
          AND status='PENDING'
    """, (reference_id,))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify(success=True)

# =============================================================
# ---------------------- ADMIN GET ALL FEEDBACKS --------------------
# =============================================================
@app.route("/admin/get_all_feedbacks")
def get_all_feedbacks():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM complaints")
        complaints = cursor.fetchall()

        cursor.execute("SELECT * FROM corrections")
        corrections = cursor.fetchall()

        cursor.execute("SELECT * FROM suggestions")
        suggestions = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify({
            "complaints": complaints,
            "corrections": corrections,
            "suggestions": suggestions
        })
    except Exception as e:
        return jsonify(error=str(e)), 500
# =============================================================
# ---------------------- ADMIN UPDATE STATUS --------------------
# =============================================================
@app.route("/admin/update_status", methods=["POST"])
def update_status():
    data = request.json
    table = data["table"]      # complaints / suggestions
    fid = data["id"]
    status = data["status"]    # RESOLVED / REJECTED

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"UPDATE {table} SET status=%s WHERE id=%s",
        (status, fid)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"success": True})

# =============================================================
# ---------------------- ADMIN REJECTS CORRECTION --------------------
# =============================================================
@app.route("/admin/reject_correction", methods=["POST"])
def reject_correction():
    try:
        data = request.get_json()
        reference_id = data.get("reference_id")

        if not reference_id:
            return jsonify(success=False, message="Reference ID missing"), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE corrections
            SET status = 'REJECTED'
            WHERE reference_id = %s
              AND status = 'PENDING'
        """, (reference_id,))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify(success=True, message="Correction rejected")

    except Exception as e:
        print("REJECT ERROR:", e)
        return jsonify(success=False, message=str(e)), 500
# =============================================================
# ---------------------- ADMIN GET FEEDBACK --------------------
# =============================================================
@app.route("/get_feedbacks", methods=["GET"])
def get_feedbacks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            c.id,
            c.user_id,
            u.voterID,
            u.fullname,
            c.field_name,
            c.old_value,
            c.new_value,
            c.status,
            c.created_at
        FROM corrections c
        JOIN users u ON c.user_id = u.id
        ORDER BY c.id DESC
    """)

    corrections = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify({"feedbacks": corrections})
# =============================================================
# ---------------------- ADMIN MARK FEEDBACK READ --------------------
# =============================================================
@app.route("/mark_feedback_read", methods=["POST"])
def mark_feedback_read():
    fid = request.json["id"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE feedback SET status='read' WHERE id=%s", (fid,))
    conn.commit()

    cursor.close()
    conn.close()
    return jsonify({"status": "success"})
# =============================================================
# ---------------------- USER OVERVIEW --------------------
# =============================================================
from datetime import date, datetime
from flask import render_template, session, redirect, url_for
import base64

@app.route("/overview")
def overview():
    user_id = session.get("user_id")

    if not user_id:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT fullname AS name, voterID, email, phone, gender, dob, face_image
        FROM users
        WHERE id = %s
    """, (user_id,))

    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user:
        return "User not found", 404

   # ---- AGE CALCULATION ----
    dob = user.get("dob")
    if dob:
        if isinstance(dob, str):
            dob = datetime.strptime(dob, "%Y-%m-%d").date()
        today = date.today()
        user["age"] = today.year - dob.year - (
            (today.month, today.day) < (dob.month, dob.day)
        )
    else:
        user["age"] = "N/A"

    # ✅ Convert image to base64
    if user.get("face_image"):
        if isinstance(user["face_image"], bytes):
            user["face_image"] = base64.b64encode(
                user["face_image"]
            ).decode("utf-8")


    # 🔥 REAL QR GENERATION
    user["qr_path"] = generate_voter_qr(
        user["voterID"],
        user["name"],
        user["phone"]
    )

    return render_template("overview.html", user=user)


# =============================================================
# ---------------------- GET USER PROFILE --------------------
# =============================================================
@app.route("/get-user-profile", methods=["POST"])
def get_user_profile():
    data = request.json or {}
    voter_id = data.get("voter_id")

    print("DEBUG get-user-profile voter_id:", voter_id)

    if not voter_id:
        return jsonify({"error": "Missing voter_id"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT fullname, email, voterID, face_image
        FROM users
        WHERE voterID = %s
    """, (voter_id,))

    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "name": user["fullname"],
        "email": user["email"],
        "voterID": user["voterID"],
	"face_image": user["face_image"]
    })

# =============================================================
# ---------------------- GET CORRECTIONS --------------------
# =============================================================
@app.route('/get_corrections', methods=['GET'])
def get_corrections():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM corrections ORDER BY id DESC")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify({"corrections": data})

# =============================================================
# ---------------------- CASTE VOTES(USER MUST LOGGED IN) --------------------
# =============================================================
@app.route("/cast_vote", methods=["POST"])
def cast_vote():
    user_id = session.get("user_id")
    candidate_id = request.json.get("candidate_id")

    if not user_id:
        return jsonify({"error": "User not logged in"}), 401

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Prevent double voting
    cursor.execute("""
        SELECT vote_id FROM votes WHERE voter_id=%s
    """, (user_id,))
    if cursor.fetchone():
        return jsonify({"error": "You have already voted"}), 403

    cursor.execute("""
        INSERT INTO votes (voter_id, candidate_id)
        VALUES (%s, %s)
    """, (user_id, candidate_id))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Vote cast successfully!"})
# =============================================================
# ---------------------- RESULTS API ---------------------------
# =============================================================
@app.route("/api/results", methods=["GET"])
def api_results():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT 
            c.candidate_code AS candidate_id,
            c.name,
            c.party,
            c.symbol,
            COALESCE(v.total_votes, 0) AS total_votes
        FROM candidates c
        LEFT JOIN candidate_votes v
            ON c.candidate_code = v.candidate_id
        WHERE c.status = 'active'
        ORDER BY total_votes DESC
    """

    cursor.execute(query)
    data = cursor.fetchall()

    print("🔥 LIVE RESULTS FROM DB:", data)  # DEBUG

    cursor.close()
    conn.close()

    return jsonify(data)
# =============================================================
# ---------------------- SEND OTP ------------------------------
# =============================================================
from datetime import datetime, timedelta
import random
from flask import request, jsonify

@app.route('/send_otp', methods=['POST'])
def send_otp():
    data = request.get_json()
    phone = data.get("phone") if data else None

    if not phone:
        return jsonify(status="error", message="Phone required"), 400

    otp = str(random.randint(1000, 9999))
    expiry = datetime.now() + timedelta(seconds=15)

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET otp=%s, otp_expiry=%s
        WHERE phone=%s
    """, (otp, expiry, phone))
    conn.commit()

    cursor.close()
    conn.close()

    # 🔥 STORE PHONE FOR OTP VERIFICATION
    session["pre_auth_phone"] = phone
    session.permanent = True

    print("OTP SENT:", otp, "TO:", phone)

    return jsonify({
        "status": "sent",
        "otp": otp   # demo only
    }), 200
# =============================================================
# ---------------------- VERIFY OTP ----------------------------
# =============================================================
from datetime import datetime
from flask import request, jsonify, session
@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    data = request.get_json()
    user_otp = data.get("otp")

    phone = session.get("pre_auth_phone")

    if not phone or not user_otp:
        return jsonify(status="error", message="OTP required"), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, voterID, fullname, otp, otp_expiry
        FROM users WHERE phone=%s
    """, (phone,))
    user = cursor.fetchone()

    if not user:
        return jsonify(status="error", message="User not found"), 404

    # ❌ OTP expired
    if not user["otp_expiry"] or user["otp_expiry"] < datetime.now():
        return jsonify(status="expired", message="OTP expired"), 401

    # ❌ OTP mismatch
    if str(user["otp"]) != str(user_otp):
        return jsonify(status="wrong", message="Invalid OTP"), 401

    # ✅ OTP SUCCESS → clear OTP
    cursor.execute("""
        UPDATE users
        SET otp=NULL, otp_expiry=NULL
        WHERE phone=%s
    """, (phone,))
    conn.commit()

    cursor.close()
    conn.close()

    # ✅ FINAL LOGIN SESSION
    session.clear()
    session["user_id"] = user["id"]
    session["phone"] = phone
    session["voter_id"] = user["voterID"]
    session.permanent = True

    add_log(
        user["voterID"],
        user["fullname"],
        "Login Successful (Password + OTP)"
    )

    return jsonify(
        status="success",
        voter_id=user["voterID"]
    ), 200
# =============================================================
# ---------------------- SYSTEM LOGS ---------------------------
# =============================================================
@app.route("/api/system-logs", methods=["GET"])
def get_system_logs():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT 
                voterID,
                fullname,
                activity,
                log_time
            FROM logs
            ORDER BY log_time DESC
            LIMIT 1000
        """)

        logs = cursor.fetchall()
        cursor.close()
        conn.close()

        return jsonify(logs)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
# =============================================================
# ---------------------- VOTING STATUS ----------------------------
# =============================================================

@app.route('/get_voting_status', methods=['GET'])
def get_voting_status():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT voting_allowed
        FROM elections
        ORDER BY election_id DESC LIMIT 1
    """)
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    return jsonify({"isVotingAllowed": bool(row["voting_allowed"])})
# =============================================================
# ---------------------- SESSION PHONE ----------------------------
# =============================================================
@app.route('/get_session_phone')
def get_session_phone():
    phone = session.get("phone")
    if phone:
        return jsonify({"phone": phone})
    return jsonify({"phone": None}), 401

# =============================================================
# ---------------------- TOGGLE VOTE ----------------------------
# =============================================================
@app.route("/toggle_voting", methods=["POST"])
def toggle_voting():
    try:
        status = request.json.get("allowed")  # 1 or 0

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE elections
            SET voting_allowed = %s
            ORDER BY election_id DESC
            LIMIT 1
        """, (status,))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Voting status updated!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# ================= UTILS =================
def base64_to_image(base64_str):
    base64_str = base64_str.split(",")[1]
    img_bytes = base64.b64decode(base64_str)
    img_array = np.frombuffer(img_bytes, np.uint8)
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return image

# ================= FACE REGISTER =================
import base64
from flask import request, jsonify
import os
from datetime import datetime

@app.route("/face-register", methods=["POST"])
def face_register():
    data = request.json
    voter_id = data.get("voter_id")
    image_base64 = data.get("image")

    if not voter_id or not image_base64:
        return jsonify({"success": False, "message": "Invalid data"})

    try:
        # Decode base64 image
        image_data = image_base64.split(",")[1]
        image_bytes = base64.b64decode(image_data)

        # Save image
        face_dir = "static/uploads/faces"
        os.makedirs(face_dir, exist_ok=True)
        image_path = f"{face_dir}/{voter_id}.jpg"

        with open(image_path, "wb") as f:
            f.write(image_bytes)

        # OPTIONAL: store path in DB (recommended)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE users
            SET face_image=%s, face_registered_at=%s
            WHERE voterID=%s
        """, (image_path, datetime.now(), voter_id))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({"success": False, "message": str(e)})


# ================= FACE VERIFY (FILE BASED – FIXED) =================
from flask import session
import os
import base64
import cv2
import numpy as np
import face_recognition

@app.route("/verify_face", methods=["POST"])
def verify_face():
    try:
        data = request.get_json()
        voter_id = data.get("voter_id")
        image_data = data.get("image")

        if not voter_id or not image_data:
            return jsonify(success=False, message="Invalid request"), 400

        # 🔹 CHECK REGISTERED FACE FILE
        registered_face_path = f"static/uploads/faces/{voter_id}.jpg"

        if not os.path.exists(registered_face_path):
            return jsonify(
                success=False,
                message="Face not registered. Please register your face first."
            )

        # 🔹 DECODE LIVE IMAGE
        live_base64 = image_data.split(",")[1]
        live_bytes = base64.b64decode(live_base64)
        live_np = np.frombuffer(live_bytes, np.uint8)
        live_img = cv2.imdecode(live_np, cv2.IMREAD_COLOR)

        if live_img is None:
            return jsonify(success=False, message="Invalid camera image")

        live_rgb = cv2.cvtColor(live_img, cv2.COLOR_BGR2RGB)

        live_faces = face_recognition.face_locations(live_rgb)

        if len(live_faces) != 1:
            return jsonify(
                success=False,
                message="Only one face should be visible"
            )

        live_encoding = face_recognition.face_encodings(
            live_rgb, live_faces
        )[0]

        # 🔹 LOAD REGISTERED IMAGE
        registered_img = face_recognition.load_image_file(
            registered_face_path
        )

        registered_faces = face_recognition.face_locations(registered_img)

        if len(registered_faces) != 1:
            return jsonify(
                success=False,
                message="Registered face image is invalid"
            )

        registered_encoding = face_recognition.face_encodings(
            registered_img, registered_faces
        )[0]

        # 🔹 COMPARE FACES
        distance = face_recognition.face_distance(
            [registered_encoding],
            live_encoding
        )[0]

        print("FACE DISTANCE:", distance)

        if distance <= 0.7:
            # 🔐 CREATE SESSION
            session["voter_id"] = voter_id
            session.permanent = True

            return jsonify(success=True, message="Face verified successfully")

        return jsonify(success=False, message="Face does not match")

    except Exception as e:
        print("FACE VERIFY ERROR:", e)
        return jsonify(success=False, message="Server error"), 500

# ================= FACE UPDATE=================
@app.route("/face-update", methods=["POST"])
def face_update():
    try:
        data = request.get_json()
        voter_id = data.get("voter_id")
        image = data.get("image")

        if not voter_id or not image:
            return jsonify(success=False, message="Missing data"), 400

        # Remove base64 header
        image = image.split(",")[1]
        image_bytes = base64.b64decode(image)

        # ---------- SAVE UPDATED IMAGE ----------
        face_dir = "static/uploads/faces"
        os.makedirs(face_dir, exist_ok=True)

        image_path = f"{face_dir}/{voter_id}.jpg"

        with open(image_path, "wb") as f:
            f.write(image_bytes)

        # ---------- FACE ENCODING ----------
        np_img = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

        face_locations = face_recognition.face_locations(img)
        if not face_locations:
            return jsonify(success=False, message="No face detected")

        face_encoding = face_recognition.face_encodings(img, face_locations)[0]
        encoding_blob = face_encoding.tobytes()

        conn = get_db_connection()
        cursor = conn.cursor()

        # Update encoding
        cursor.execute("""
            UPDATE voter_faces
            SET face_encoding=%s
            WHERE voter_id=%s
        """, (encoding_blob, voter_id))

        # Update stored image path
        cursor.execute("""
            UPDATE users
            SET face_image=%s, face_registered_at=NOW()
            WHERE voterID=%s
        """, (image_path, voter_id))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify(success=True)

    except Exception as e:
        print("FACE UPDATE ERROR:", e)
        return jsonify(success=False, message="Server error"), 500

# ================= VERIFY LIVENESS =================
@app.route("/verify-liveness", methods=["POST"])
def verify_liveness():
    frames = request.json.get("frames", [])

    if len(frames) < 5:
        return jsonify({"live": False})

    images = [decode_image(f) for f in frames]

    texture_vals = [texture_score(img) for img in images]
    motion_vals = [
        motion_score(images[i], images[i+1])
        for i in range(len(images)-1)
    ]

    avg_texture = np.mean(texture_vals)
    avg_motion = np.mean(motion_vals)

    print("Texture:", avg_texture, "Motion:", avg_motion)

    if avg_texture < 15:
        return jsonify({"live": False})

    if avg_motion < 1.0:
        return jsonify({"live": False})

    return jsonify({"live": True})

# ================= TRACK STATUS =================
@app.route("/track_feedback_status", methods=["POST"])
def track_feedback_status():
    try:
        data = request.get_json()
        reference_id = data.get("reference_id", "").strip().upper()
        feedback_type = data.get("feedback_type", "").strip().lower()

        print("REFERENCE RECEIVED:", reference_id, "TYPE:", feedback_type)

        if not reference_id or not feedback_type:
            return jsonify(found=False, message="Missing input"), 400

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        if feedback_type == "correction":
            cursor.execute("""
                SELECT reference_id, voter_id, field_name, old_value, new_value,
                       status, created_at
                FROM corrections
                WHERE reference_id = %s
            """, (reference_id,))
            row = cursor.fetchone()
            if row:
                cursor.close()
                conn.close()
                return jsonify(
                    found=True,
                    feedback_type="CORRECTION",
                    reference_id=row["reference_id"],
                    voter_id=row["voter_id"],
                    field_name=row.get("field_name"),
                    old_value=row.get("old_value"),
                    new_value=row.get("new_value"),
                    status=row["status"].lower(),
                    created_at=row["created_at"].strftime("%d %b %Y")
                )

        elif feedback_type == "complaint":
            cursor.execute("""
                SELECT reference_id, voter_id, message,
                       status, created_at
                FROM complaints
                WHERE reference_id = %s
		LIMIT 1
            """, (reference_id,))
            row = cursor.fetchone()
            if row:
                cursor.close()
                conn.close()
                return jsonify(
                    found=True,
                    feedback_type="COMPLAINT",
                    reference_id=row["reference_id"],
                    voter_id=row["voter_id"],
                    message=row.get("message"),
                    status=row["status"],
                    created_at=row["created_at"].strftime("%d %b %Y")
                )

        elif feedback_type == "suggestion":
            cursor.execute("""
                SELECT reference_id, voter_id, message,
                       status, created_at
                FROM suggestions
                WHERE reference_id = %s
		LIMIT 1
            """, (reference_id,))
            row = cursor.fetchone()
            if row:
                cursor.close()
                conn.close()
                return jsonify(
                    found=True,
                    feedback_type="SUGGESTION",
                    reference_id=row["reference_id"],
                    voter_id=row["voter_id"],
                    message=row.get("message"),
                    status=row["status"],
                    created_at=row["created_at"].strftime("%d %b %Y")
                )

        cursor.close()
        conn.close()
        return jsonify(found=False)

    except Exception as e:
        print("TRACK ERROR:", e)
        return jsonify(found=False, error=str(e)), 500

# ================= CHANGE PASSWORD =================
from flask import request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/change-password-secure', methods=['POST'])
def change_password_secure():
    data = request.json
    user_id = session.get('user_id')

    if not user_id:
        return jsonify(status="error", message="Not logged in"), 401

    old_pass_input = data.get('old_password')
    new_pass_input = data.get('new_password')

    if not old_pass_input or not new_pass_input:
        return jsonify(status="error", message="Missing fields"), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT password_hash, voterID, fullname FROM users WHERE id=%s",
        (user_id,)
    )
    user = cursor.fetchone()

    if not check_password_hash(user['password_hash'], old_pass_input):
        return jsonify(status="error", message="Current password is wrong"), 400

    if check_password_hash(user['password_hash'], new_pass_input):
        return jsonify(status="error", message="New password must be different"), 400

    new_hash = generate_password_hash(new_pass_input)

    cursor.execute(
        "UPDATE users SET password_hash=%s WHERE id=%s",
        (new_hash, user_id)
    )
    conn.commit()

    cursor.close()
    conn.close()

    add_log(user['voterID'], user['fullname'], "Password Updated")

    return jsonify(success=True), 200
# =============================================================
# -------------------- SAVE FCM TOKEN -------------------------
# =============================================================
@app.route("/save-fcm-token", methods=["POST"])
def save_fcm_token():
    try:
        data = request.get_json()
        print("FCM DATA RECEIVED:", data)

        if not data:
            return jsonify(success=False, message="No JSON received"), 400

        voter_id = data.get("voter_id")
        fcm_token = data.get("fcm_token")

        if not voter_id or not fcm_token:
            return jsonify(success=False, message="Missing voter_id or token"), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO fcm_tokens (voter_id, fcm_token)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE fcm_token = VALUES(fcm_token)
        """, (voter_id, fcm_token))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify(success=True, message="FCM token saved"), 200

    except Exception as e:
        print("SAVE FCM TOKEN ERROR:", e)
        return jsonify(success=False, error=str(e)), 500
# =============================================================
# ---------------------- SEND NOTIFICATION -----------------------
# =============================================================
@app.route("/send-test-notification", methods=["POST"])
def send_test_notification():
    cursor.execute("SELECT fcm_token FROM fcm_tokens LIMIT 1")
    token = cursor.fetchone()[0]

    send_push(
        token,
        "MATDAANSECURE 🇮🇳",
        "Voting has started. Please vote now."
    )

    return {"success": True}
# =============================================================
# ADMIN: START VOTING + NOTIFY ALL VOTERS
# =============================================================
@app.route("/admin/start-voting", methods=["POST"])
def admin_start_voting():
    conn = get_db_connection()
    cursor = conn.cursor()

    # (Optional) update voting status
    cursor.execute(
        "UPDATE system_status SET voting_status='STARTED'"
    )
    conn.commit()

    # Fetch all FCM tokens
    cursor.execute("SELECT fcm_token FROM fcm_tokens")
    tokens = cursor.fetchall()

    for (token,) in tokens:
        message = messaging.Message(
            notification=messaging.Notification(
                title="MATDAANSECURE 🇮🇳",
                body="Voting has officially started. Please cast your vote."
            ),
            token=token
        )
        messaging.send(message)

    cursor.close()
    conn.close()

    return jsonify(success=True, message="Voting started and notifications sent")

# =============================================================
# ADMIN: SEND CUSTOM ALERT
# =============================================================
@app.route("/admin/send-alert", methods=["POST"])
def admin_send_alert():
    data = request.get_json()
    title = data.get("title")
    body = data.get("body")

    if not title or not body:
        return jsonify(success=False, message="Missing title or body"), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # ✅ SAVE notification
    cursor.execute(
        "INSERT INTO notifications (title, body) VALUES (%s, %s)",
        (title, body)
    )
    conn.commit()

    # ✅ SEND push notifications
    cursor.execute("SELECT fcm_token FROM fcm_tokens")
    tokens = cursor.fetchall()

    for (token,) in tokens:
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body
            ),
            token=token
        )
        messaging.send(message)

    cursor.close()
    conn.close()

    return jsonify(success=True, message="Alert sent to all users")

# =============================================================
# GET NOTIFICATIONS
# =============================================================
@app.route("/get-notifications")
def get_notifications():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT title, body, created_at
        FROM notifications
        ORDER BY created_at DESC
    """)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)

# =============================================================
# NOTIFICATIONS UNREAD COUNT
# =============================================================
@app.route("/notifications/unread-count")
def unread_notification_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM notifications WHERE is_read = 0")
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return jsonify(count=count)

# =============================================================
# NOTIFICATIONS MARK READ
# =============================================================
@app.route("/notifications/mark-read", methods=["POST"])
def mark_notifications_read():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE notifications SET is_read = 1 WHERE is_read = 0")
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(success=True)


# =============================================================
# FINAL PERMANENT VOTE RECEIPT (Styled Preview)
# =============================================================

from flask import send_file, session
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image,
    Table, TableStyle, PageTemplate, Frame
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.lib.units import cm
import os

@app.route("/preview-vote-receipt")
def preview_vote_receipt():

    # ---------------- SESSION DATA ----------------
    voter_id = session.get("voter_id")

    if not voter_id:
        return "Please login again.", 401

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT candidate_id, vote_proof_id, voted_at
        FROM votes
        WHERE voter_id = %s
        LIMIT 1
    """, (voter_id,))

    vote = cursor.fetchone()
    cursor.close()
    conn.close()

    if not vote:
        return "Error: Vote not found.", 404

    vote_proof_id = vote.get("vote_proof_id")
    if not vote_proof_id:
        return "Error: Vote proof ID missing. Contact administrator.", 500

    candidate = vote["candidate_id"]
    voted_at = vote["voted_at"].strftime("%d %B %Y, %I:%M %p")
    voter_photo = f"static/uploads/faces/{voter_id}.jpg"

    os.makedirs("vote_receipts", exist_ok=True)
    file_path = f"vote_receipts/Final_Receipt_{voter_id}.pdf"

    # ---------------- BACKGROUND WATERMARK ----------------
    def draw_background(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica-Bold", 25)
        canvas.setFillColorRGB(0.94, 0.94, 0.94)
        canvas.rotate(35)
        for x in range(-500, 1200, 250):
            for y in range(-800, 1200, 120):
                canvas.drawString(x, y, "MATDAANSECURE")
        canvas.restoreState()

    # ---------------- VOTED STAMP ----------------
    def draw_stamp(canvas, doc):
    	canvas.saveState()
    	canvas.setStrokeColorRGB(0.8, 0.2, 0.2)
    	canvas.setFillColorRGB(0.8, 0.2, 0.2)
    	canvas.setLineWidth(2.5)
    	canvas.translate(485, 585)
    	canvas.rotate(28)
    	canvas.roundRect(-45, -15, 90, 30, 4, stroke=1, fill=0)
    	canvas.setFont("Helvetica-Bold", 18)
    	canvas.drawCentredString(0, -5, "VOTED")
    	canvas.restoreState()

    # ---------------- DOCUMENT SETUP ----------------
    doc = SimpleDocTemplate(file_path, pagesize=A4, topMargin=50)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height)

    template = PageTemplate(
        id="receipt",
        frames=[frame],
        onPage=draw_background,
        onPageEnd=draw_stamp
    )
    doc.addPageTemplates([template])

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="MainTitle",
        fontSize=22,
        alignment=1,
        spaceAfter=30,
        fontName="Helvetica-Bold"
    ))
    styles.add(ParagraphStyle(
        name="SubTitle",
        fontSize=14,
        alignment=1,
        spaceAfter=30
    ))
    styles.add(ParagraphStyle(
        name="Label",
        fontSize=10,
        fontName="Helvetica-Bold"
    ))
    styles.add(ParagraphStyle(
        name="Value",
        fontSize=10
    ))
    styles.add(ParagraphStyle(
        name="Body",
        fontSize=10,
        leading=14
    ))

    story = []

    # ---------------- HEADER ----------------
    story.append(Paragraph("MATDAANSECURE", styles["MainTitle"]))
    story.append(Paragraph("Official Vote Confirmation Receipt", styles["SubTitle"]))

    # ---------------- DETAILS TABLE ----------------
    details = [
        ["Voter Proof ID:", vote_proof_id],
        ["Voter ID:", voter_id],
        ["Voted Candidate:", candidate],
        ["Date & Time:", voted_at],
    ]

    left_table = Table(details, colWidths=[4 * cm, 7 * cm])
    left_table.setStyle(TableStyle([
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ]))

    if os.path.exists(voter_photo):
        photo = Image(voter_photo, width=4 * cm, height=5 * cm)
    else:
        photo = Paragraph("PHOTO NOT FOUND", styles["Label"])

    story.append(Table([[left_table, photo]], colWidths=[11 * cm, 5 * cm]))
    story.append(Spacer(1, 30))

    # ---------------- DISCLAIMER ----------------
    story.append(Paragraph(
        "This receipt confirms that the above voter cast their vote using the "
        "<b>MATDAANSECURE Online Voting System</b>. "
        "Identity verification was completed via facial authentication. "
        "This document is system-generated and does not require signature.",
        styles["Body"]
    ))

    story.append(Spacer(1, 40))

    # ---------------- QR CODE ----------------
    qr_text = f"""
MATDAANSECURE – Vote Verification

Vote Proof ID : {vote_proof_id}
Voter ID      : {voter_id}
Candidate     : {candidate}
Voted At      : {voted_at}

Status        : VERIFIED
"""

    qr_widget = qr.QrCodeWidget(qr_text)

    bounds = qr_widget.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]

    d = Drawing(
        120, 120,
        transform=[120/width, 0, 0, 120/height, 0, 0]
    )
    d.add(qr_widget)
    d.hAlign = "CENTER"

    story.append(d)
    story.append(Spacer(1, 8))
    story.append(Paragraph('<para align="center">Scan QR Code to Verify Vote</para>', styles["Label"]))

    # ---------------- FOOTER ----------------
    story.append(Spacer(1, 40))
    footer = Table(
        [["Empowering Democracy, One Click At A Time"]],
        colWidths=[17 * cm]
    )
    footer.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.lightgrey),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Oblique"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))

    story.append(footer)

    doc.build(story)
    return send_file(
	file_path,
	as_attachment=True,
	download_name=f"Vote_Proof_{voter_id}.pdf"
    )

# =============================================================
# RESET PASSWORD
# =============================================================
@app.route('/reset_password', methods=['POST'])
def reset_password_api():
    email = request.form.get('email')
    new_password = request.form.get('password')

    if not email or not new_password:
        return jsonify({"status": "error", "message": "Missing data"}), 400

    hashed_password = generate_password_hash(new_password)

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET password_hash=%s,
            otp=NULL,
            otp_expiry=NULL
        WHERE email=%s
    """, (hashed_password, email))

    conn.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return jsonify({"status": "error", "message": "Email not found"}), 404

    cursor.close()
    conn.close()

    # 🔐 Kill any existing session
    session.clear()

    return jsonify({
        "status": "success",
        "message": "Password updated successfully"
    }), 200
# =============================================================
# ADMIN DASHBOARD STATS
# =============================================================
@app.route("/admin/dashboard-stats")
def admin_dashboard_stats():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total_votes FROM votes")
    total_votes = cursor.fetchone()["total_votes"]

    cursor.execute("SELECT COUNT(*) AS total_voters FROM users")
    total_voters = cursor.fetchone()["total_voters"]

    cursor.execute("SELECT COUNT(*) AS total_candidates FROM candidates WHERE status='Active'")
    total_candidates = cursor.fetchone()["total_candidates"]

    cursor.close()
    conn.close()

    return jsonify({
        "totalVotes": total_votes,
        "totalVoters": total_voters,
        "totalCandidates": total_candidates
    })

# =============================================================
# ADMIN VOTES OVERTIME
# =============================================================
@app.route("/admin/votes-over-time")
def votes_over_time():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT DATE(voted_at) AS vote_date, COUNT(*) AS total
        FROM votes
        GROUP BY DATE(voted_at)
        ORDER BY vote_date
    """)

    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(data)

# =============================================================
# ADMIN VOTER TYPE
# =============================================================
@app.route("/admin/voter-type-distribution")
def voter_type_distribution():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT user_type, COUNT(*) AS total
        FROM users
        GROUP BY user_type
    """)

    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(data)
# =============================================================
# ADMIN CANDIDATE VOTES
# =============================================================
@app.route("/admin/candidate-votes")
def candidate_votes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT c.name, COUNT(v.id) AS votes
        FROM candidates c
        LEFT JOIN votes v ON v.candidate_id = c.id
        WHERE c.status='Active'
        GROUP BY c.id
        ORDER BY votes DESC
    """)

    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(data)


# =============================================================
# ELECTOR ROLL CALL
# =============================================================
@app.route("/api/get_voters", methods=["GET"])
def get_voters():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT 
                voterID AS id,
                fullname AS name,
                email,
                phone
            FROM users
        """
        cursor.execute(query)
        voters = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(voters)

    except Exception as e:
        print("Error fetching voters:", e)
        return jsonify({"error": "Unable to fetch voter data"}), 500

# =============================================================
# ADMIN LIVE VOTERS
# =============================================================
@app.route("/admin/api/voters", methods=["GET"])
def admin_get_voters():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT 
                voterID,
                fullname,
                email,
                phone
            FROM users
            WHERE user_type != 'admin'
            ORDER BY voterID ASC
        """)

        users = cursor.fetchall()

        for u in users:
            u["status"] = "Not Voted"

        cursor.close()
        conn.close()

        return jsonify({
            "success": True,
            "data": users
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
# ============================================================
# ADMIN ANALYTICS
# ============================================================
def get_count(cursor, query):
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0] if result else 0

@app.route("/admin/analytics", methods=["GET"])
def admin_analytics_v2():
    conn = get_db_connection()
    cursor = conn.cursor()

    # ---------------- USERS & VOTES ----------------
    total_voters = get_count(cursor, "SELECT COUNT(*) FROM users")
    votes_cast = get_count(cursor, "SELECT COUNT(*) FROM votes")
    did_not_vote = total_voters - votes_cast

    # ---------------- FEEDBACK TABLES ----------------
    suggestions = get_count(cursor, "SELECT COUNT(*) FROM suggestions")
    complaints = get_count(cursor, "SELECT COUNT(*) FROM complaints")
    corrections = get_count(cursor, "SELECT COUNT(*) FROM corrections")

    cursor.close()
    conn.close()

    return jsonify({
        "activity": {
            "voters_registered": total_voters,
            "votes_cast": votes_cast,
            "did_not_vote": did_not_vote
        },
        "feedback": {
            "suggestions": suggestions,
            "complaints": complaints,
            "corrections": corrections
        }
    })

# ============================================================
# ADMIN ANNOUNCEMENT MANAGEMENT (MULTIPLE + SPEED)
# ============================================================

@app.route("/admin/announcements", methods=["GET", "POST"])
def manage_announcements():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_PASSWORD",
            database="matdaansecure"
        )

        cursor = conn.cursor(dictionary=True)

        # ================= GET =================
        if request.method == "GET":
            cursor.execute("SELECT * FROM announcements ORDER BY id ASC")
            rows = cursor.fetchall()

            announcements = [row["message"] for row in rows]
            speed = rows[0]["speed"] if rows else 20

            cursor.close()
            conn.close()

            return jsonify({
                "announcements": announcements,
                "speed": speed
            })

        # ================= POST =================
        if request.method == "POST":
            data = request.get_json()
            announcements = data.get("announcements", [])
            speed = data.get("speed", 20)

            # Clear old announcements
            cursor.execute("DELETE FROM announcements")

            # Insert new ones
            for message in announcements:
                cursor.execute(
                    "INSERT INTO announcements (message, speed) VALUES (%s, %s)",
                    (message, speed)
                )

            conn.commit()
            cursor.close()
            conn.close()

            return jsonify({"status": "success"})

    except Exception as e:
        print("ANNOUNCEMENT ERROR:", e)
        return jsonify({"status": "error"})


# ============================================================
# END OF API ROUTES
# ============================================================

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5001)
