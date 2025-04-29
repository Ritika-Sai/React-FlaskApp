from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# We'll still use Flask-CORS as a base configuration
CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "supports_credentials": True}})

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

def validate_user(username, password):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()
    
    if user and check_password_hash(user['password'], password):
        return True
    else:
        return False
    
def create_database():
    import sqlite3
    from werkzeug.security import generate_password_hash

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Example: Add a user. Remember to hash the password.
    hashed_password = generate_password_hash('password')
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('testuser', hashed_password))
    conn.commit()
    conn.close()

def create_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        hashed_password = generate_password_hash(password)
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Duplicate username
    finally:
        conn.close()

# Helper function to add CORS headers to all responses
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/')
def home():
    response = make_response('Flask server is running!')
    return add_cors_headers(response)

@app.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = make_response()
        return add_cors_headers(response)
        
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_is_valid = validate_user(username, password)
    
    if user_is_valid:
        response = make_response(jsonify({'message': 'Login successful!'}))
    else:
        response = make_response(jsonify({'message': 'Invalid credentials.'}), 401)
    
    return add_cors_headers(response)
    
@app.route('/signup', methods=['POST', 'OPTIONS'])
def signup():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = make_response()
        return add_cors_headers(response)
        
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if create_user(username, password):
        response = make_response(jsonify({'message': 'Signup successful!'}), 201)
    else:
        response = make_response(jsonify({'message': 'Username already exists.'}), 409)
    
    return add_cors_headers(response)

# Add CORS headers to all responses
@app.after_request
def after_request(response):
    return add_cors_headers(response)

if __name__ == '__main__':
    # run create_database only the first time
    # create_database()
    app.run(debug=True)