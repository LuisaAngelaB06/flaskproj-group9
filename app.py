from flask import Flask, render_template
from dotenv import load_dotenv
from config import Config
import os

load_dotenv()

app = Flask(__name__)

app.config.from_object(Config)

# Login page route
@app.route('/')
def login():
    return render_template('login-page.html')

# Register page route
@app.route('/register')
def register():
    return render_template('register-page.html')

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5055))
    app.run(debug=True, port=port)