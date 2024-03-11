import requests
from datetime import datetime
import os

# Replace 'your_github_token' with your actual GitHub token
github_token = os.getenv("GITHUB_TOKEN")
print(f'GitHub Token: {github_token}')
url = 'https://api.github.com/rate_limit'
headers = {'Authorization': f'Bearer {github_token}'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    resources = data['resources']

    # Initialize an empty string to store the information
    response_text = ""

    for resource_type, details in resources.items():
        limit = details['limit']
        used = details['used']
        remaining = details['remaining']
        reset_timestamp = details['reset']

        # Convert the timestamp to a human-readable format in 12-hour format
        reset_time = datetime.utcfromtimestamp(reset_timestamp).strftime('%Y-%m-%d %I:%M:%S %p')

        # Concatenate the information
        response_text += (
            f'{resource_type.capitalize()} Resources:\n'
            f'  Limit: {limit}\n'
            f'  Used: {used}\n'
            f'  Remaining: {remaining}\n'
            f'  Reset time: {reset_time}\n\n'
        )

    # Assuming message is the object for sending replies
    print(response_text.strip())
else:
    error_text = f'Error: {response.status_code}'
    print(error_text)
