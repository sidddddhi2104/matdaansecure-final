from werkzeug.security import generate_password_hash

password = "admin123"   # Change to your desired admin password
print(generate_password_hash(password))
