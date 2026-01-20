# Day 20: PIP & APIs - Fetching Real-World Data
# Using the 'requests' library to interact with external APIs.

import requests
import json

# 1. Target a public API (Example: Random User Generator)
URL = "https://randomuser.me/api/"

try:
    # 2. GET Request: Fetching data from the web
    response = requests.get(URL)
    
    # 3. Validation: Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # 4. Extracting specific features
        user = data['results'][0]
        name = f"{user['name']['first']} {user['name']['last']}"
        location = user['location']['city']
        
        print(f"✅ Successfully fetched data for: {name}")
        print(f"🌍 Location: {location}")
        
        # 5. Saving this "External Data" to a local file (Day 19 Skill!)
        with open("latest_user.json", "w") as f:
            json.dump(user, f, indent=4)

except Exception as e:
    print(f"❌ API Connection Error: {e}")