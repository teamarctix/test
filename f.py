import asyncio
import subprocess
import os
from pyrogram import Client

api_id = 11405252
api_hash = "b1a1fc3dc52ccc91781f33522255a880"
bot_token2 = "6593397412:AAFmJ8Hj9jnZuvLs_rLcu63bQwCp0EV829w"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token2)

up = {"ytdl": False, 'Total': 0}

links = ["https://www.pornhub.com/playlist/85569291"]

async def progress(current, total, task_name="Task"):
    percentage = current * 100 / total
    bar_length = 20
    completed_blocks = int(bar_length * current / total)
    bar = "█" * completed_blocks + " " * (bar_length - completed_blocks)
    print(f"{task_name} Progress: [{bar}] {percentage:.1f}% Complete")

async def download_and_upload(link):
    try:
        # Download video
        subprocess.run(
            ["yt-dlp", "--downloader", "aria2c", "--match-filter", "duration>180", "--max-downloads", "200",
             "-N", "10", "-o", "%(title)s.%(ext)s", "-f", "(mp4)[height=?720]", "--write-thumbnail", "--embed-metadata", link],
            check=True
        )

        print(f"Download Completed: {link}")
        await asyncio.sleep(120)  # Sleep asynchronously

        # Set ytdl flag to True
        up["ytdl"] = True

    except subprocess.CalledProcessError as e:
        print(f"Error during download: {e}")

async def upload_video(filename, sts_id):
    try:
        # Add video processing here if needed
        os.system(f'''vcsi "{filename}" -g 2x2 --metadata-position hidden -o "{filename.replace('.mp4','.png')}" ''')

        # Update status message
        await app.edit_message_text(-1002034630043, sts_id, f"Uploaded Videos: {up['Total']}\nUploading {filename}")

        # Send video
        video = await app.send_video(-1002034630043, video=filename, caption=filename.replace(".mp4", ""),
                                      thumb=filename.replace(".mp4", ".png"), supports_streaming=True, progress=progress)

        # Update status message after upload
        up['Total'] += 1
        await app.edit_message_text(-1002034630043, sts_id, f"Uploaded Videos: {up['Total']}\nUploaded {filename}")

        # Remove files
        os.remove(filename)
        os.remove(filename.replace('.mp4', '.png'))
        await app.edit_message_text(-1002034630043, sts_id, f"Uploaded Videos: {up['Total']}\nCleared {filename}")

    except Exception as e:
        print(e)

async def main():
    async with app:
        for link in links:
            # Download and set up initial status message
            sts = await app.send_message(-1002034630043, f"Downloading {link}")
            await download_and_upload(link)

            # Check for uploaded flag
            while not up["ytdl"]:
                for filename in os.listdir():
                    if filename.endswith(".mp4"):
                        await upload_video(filename, sts.id)

                await asyncio.sleep(6)

if __name__ == "__main__":
    print("Bot Started")
    app.run(main())
