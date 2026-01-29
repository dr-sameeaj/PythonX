# Day 29: System Integration - Pandas meets Flask
# Using a professional data engine to power our Web API.

import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# 1. Load Data into Pandas (The ML Brain)
# In a real scenario, this could be pd.read_csv('events.csv')
raw_data = {
    'name': ['Astro Quiz', 'Stargazing', 'Python Workshop', 'Fintech Talk', 'Deep Sky Expo'],
    'dept': ['AstroClub', 'AstroClub', 'CSE', 'Finance', 'AstroClub'],
    'popularity': [85, 92, 78, 65, 95]
}
df = pd.DataFrame(raw_data)

@app.route('/api/recommend', methods=['GET'])
def recommend_events():
    # 2. Logic: Use Pandas to find 'High Popularity' events
    # We are serving only events with popularity > 80
    threshold = int(request.args.get('min_pop', 80))
    
    # Pandas filtering is much faster and cleaner than manual loops
    recommendations = df[df['popularity'] >= threshold]
    
    # Convert Pandas result back to JSON for the web
    return jsonify({
        "status": "success",
        "count": len(recommendations),
        "data": recommendations.to_dict(orient='records')
    })

if __name__ == '__main__':
    app.run(debug=True)