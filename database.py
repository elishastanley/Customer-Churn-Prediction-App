import sqlite3
import bcrypt

DATABASE_NAME = "churn.db"


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def authenticate(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password FROM users WHERE username = ?", (username,))
    db_password = cursor.fetchone()
    conn.close()
    if db_password:
        # Ensure db_password[0] is treated as bytes
        db_password = db_password[0]
        if isinstance(db_password, str):
            db_password = db_password.encode('utf-8')
        # Ensure the plaintext password is encoded to bytes
        password = password.encode('utf-8')
        # Check if the encoded plaintext password matches the stored hashed password
        if bcrypt.checkpw(password, db_password):
            return True
    return False
