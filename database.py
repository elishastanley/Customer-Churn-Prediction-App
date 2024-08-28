import sqlite3
import bcrypt

DATABASE_NAME = "churn.db"


def get_connection():
    """Create and return a connection to the database."""
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def authenticate(username, password):
    """Authenticate a user with username and password."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password FROM users WHERE username = ?", (username,))
    db_password = cursor.fetchone()
    conn.close()
    if db_password:
        db_password = db_password[0]
        if isinstance(db_password, str):
            db_password = db_password.encode('utf-8')
        password = password.encode('utf-8')
        if bcrypt.checkpw(password, db_password):
            return True
    return False
