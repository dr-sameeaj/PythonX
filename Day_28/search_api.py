# Day 28: API Endpoints - The Search Engine
# Connecting user queries to our data logic.

from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated Database of AstroClub & GLA Events
event_db = [
    {"id": 1, "name": "Astronomy Quiz", "type": "Quiz", "points": 10},
    {"id": 2, "name": "Stargazing Night", "type": "Workshop", "points": 20},
    {"id": 3, "name": "Telescope Making", "type": "Workshop", "points": 50},
    {"id": 4, "name": "Python for Space", "type": "Seminar", "points": 15}
]

@app.route('/search', methods=['GET'])
def search_events():
    # 1. Capture the query parameter 'q' from the URL
    query = request.args.get('q', '').lower()
    
    # 2. Logic: Filter the database based on the search term
    # This mimics a search engine or an AI retrieval system
    results = [e for e in event_db if query in e['name'].lower() or query in e['type'].lower()]
    
    return jsonify({
        "status": "success",
        "count": len(results),
        "query": query,
        "data": results
    })

if __name__ == '__main__':
    app.run(debug=True)