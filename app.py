from flask import Flask, render_template
import os

app = Flask(__name__)

# Home route (optional — you can later create an index.html)
@app.route('/')
def home():
    return "Welcome to our Flask project!"

# Login page route
@app.route('/login')
def login():
    return render_template('login-page.html')

# Register page route
@app.route('/register')
def register():
    return render_template('register-page.html')

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5055))
    app.run(debug=True, port=port)