# Day 26: Flask Basics - The Birth of Eventopia
# Creating a web server to host our university event portal.

from flask import Flask

# 1. Initialize the Flask application
app = Flask(__name__)

# 2. Define the 'Route' (The URL address)
@app.route('/')
def home():
    # This is what the user sees in their browser
    return """
    <h1>Welcome to Eventopia 🚀</h1>
    <p>Your 1-point destination for all GLA University events!</p>
    <hr>
    <h3>Current Status:</h3>
    <ul>
        <li>System: Online</li>
        <li>Challenge: Day 26/30</li>
    </ul>
    """

# 3. Run the application
if __name__ == '__main__':
    # debug=True allows the server to auto-reload when you save changes
    app.run(debug=True)