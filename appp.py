import requests
from datetime import datetime
import os

def get_forks(repo_link):
    try:
        # Adding the access token to the headers for authentication
        headers = {'Authorization': f'token {os.getenv("GITHUB_TOKEN")}'}

        # Initialize an empty list to store all forks
        all_forks = []

        # Fetching fork data from the API with pagination
        while True:
            response = requests.get(repo_link, headers=headers)
            response.raise_for_status()  # Raise an HTTPError for bad responses

            forks_data = response.json()

            # Check if the access token has limitations
            if 'X-RateLimit-Remaining' in response.headers:
                remaining_limit = int(response.headers['X-RateLimit-Remaining'])
                if remaining_limit == 0:
                    reset_time = int(response.headers['X-RateLimit-Reset'])
                    reset_time_formatted = datetime.utcfromtimestamp(reset_time).strftime('%Y-%m-%d %H:%M:%S UTC')
                    print(f"Access token rate limit reached. Reset time: {reset_time_formatted}")
                    break

            # If there are no more pages, break the loop
            if 'next' not in response.links:
                break

            # Update the repo_link for the next page
            repo_link = response.links['next']['url']

            # Append all forks to the list
            all_forks.extend(forks_data)

        # Sort forks by creation time in descending order
        sorted_forks = sorted(all_forks, key=lambda x: x['created_at'], reverse=True)

        # Extracting fork links
        fork_links = [fork['html_url'] for fork in sorted_forks]

        return fork_links

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        print(f"Response content: {response.content}")
        print(f"Request URL: {repo_link}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")

    return None

def save_to_txt(fork_links, filename="wzmlx-fork.txt"):
    try:
        with open(filename, 'w') as file:
            for link in fork_links:
                file.write(link + '\n')
        print(f"Fork links saved to {filename}")

    except IOError as e:
        print(f"Error saving to file: {e}")

def save_token_to_env(token):
    try:
        # Save the GitHub token to a .env file
        with open(".env", "w") as env_file:
            env_file.write(f"GITHUB_TOKEN={token}\n")
        print("GitHub token saved to .env file")

    except IOError as e:
        print(f"Error saving token to .env file: {e}")

# Example usage with access token from environment variable and saving to a TXT file
repo_link = "https://api.github.com/repos/anasty17/mirror-leech-telegram-bot/forks"
result = get_forks(repo_link)

if result:
    save_to_txt(result)
    save_token_to_env(os.getenv("GITHUB_TOKEN"))
else:
    print("Script execution encountered an issue.")
