from flask import Flask, jsonify

app = Flask(__name__)

# Simulated Database (from your Pandas/ML logic)
events = [
    {"id": 1, "name": "Astro Quiz", "dept": "AstroClub"},
    {"id": 2, "name": "Python Hackathon", "dept": "CSE"},
    {"id": 3, "name": "Stargazing", "dept": "AstroClub"}
]

@app.route('/')
def home():
    return "<h1>Eventopia ML Dashboard</h1><p>Navigate to /api/events to see raw data.</p>"

# This is an API route - essential for AI to send/receive data

@app.route('/api/events')
def get_events():
    return jsonify(events)

# Dynamic Route: Filter events by department
@app.route('/api/events/<department>')
def filter_events(department):
    filtered = [e for e in events if e['dept'].lower() == department.lower()]
    return jsonify(filtered)

if __name__ == '__main__':
    app.run(debug=True)