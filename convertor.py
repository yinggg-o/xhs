


# Read the cookies.txt file
cookies_txt_file = "cookies.txt"  # Update with the correct path

with open(cookies_txt_file, 'r') as file:
    lines = file.readlines()  # Read all lines from the file

import json
from datetime import datetime

# Define a list to hold cookies as dictionaries
cookies_list = []

for line in lines:
    # Ignore empty lines and comments
    if line.startswith("#") or line.strip() == "":
        continue
    
    # Split the line into its components (tab-separated)
    parts = line.strip().split("\t")
    
    # Extract the necessary fields
    cookie = {
        'domain': parts[0],
        'hostOnly': parts[1] == "FALSE",  # Convert "TRUE" or "FALSE" to boolean
        'path': parts[2],
        'secure': parts[3] == "TRUE",  # Convert "TRUE" or "FALSE" to boolean
        'expirationDate': int(parts[4]),  # Expiry as UNIX timestamp
        'name': parts[5],
        'value': parts[6],
    }
    
    # Add the cookie to the list
    cookies_list.append(cookie)

# Convert the list of dictionaries to JSON
cookies_json = json.dumps(cookies_list, indent=4)  # Pretty-print with indentation

# Save to a JSON file
cookies_json_file = "cookies.json"  # Update with the desired output path
with open(cookies_json_file, 'w') as json_file:
    json_file.write(cookies_json)

print(f"Cookies converted and saved to {cookies_json_file}")
