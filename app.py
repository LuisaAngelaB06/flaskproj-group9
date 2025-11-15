from dotenv import Load_dotenv
import os

Load_dotenv()

from flask import Flask, render_template
import os

app = Flask(__name__)

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