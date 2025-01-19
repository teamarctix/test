#from spdatabase import *
from pyrogram import Client, filters
import requests,os,csv
from time import time
import time
from datetime import datetime
from pytz import *
import pytz
from pyrogram import enums

#create_table()

api_id = 3702208
api_hash = "3ee1acb7c7622166cf06bb38a19698a9"
bot_token = "5030635324:AAEaM9t5WBQHUeUAfJJK4r39h5457YwuD1k"




app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

app2 = Client(
    "my_bot2",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)



def stats(status,crtda,total):
    stats = f'<b>├  Status: </b>{status}\n'\
            f'<b>├  Uploaded Videos: </b>{total}\n'\
            f'<b>╰ Updated Time: </b>{crtda}\n\n'
    return stats


async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")

async def main():
   async with app:
     count = 0
     now=datetime.now(pytz.timezone("Asia/Kolkata"))
     crtda = now.strftime('%m/%d %H:%M %p')
     #mssg = await app.send_message(-1001984459303,"Status:")
     #print(stats("Active",crtda,"Uploading.."))
     await app.edit_message_text(-1001984459303,4,text=stats("Active",crtda,"Uploading.."))
     for  filename in os.listdir():
      if filename.endswith(".mp4"):
            count+=1
            os.system(f'''vcsi """{filename}""" -g 2x6 --metadata-position hidden -o """{filename.replace('.mp4','.png')}""" ''')
            video = await app.send_video(-10011924131916, video=filename,caption=filename.replace(".mp4",""),thumb=filename.replace(".mp4",".jpg"),progress=progress)
            vid = f"https://t.me/c/1737315050/{video.id}"
            pic = await app.send_photo(-1001850809351, photo=filename.replace(".mp4",".png"))   
            os.system(f'''rclone --config './rclone.conf' move """{filename.replace('.mp4','.jpg')}"""  'PH_Pics:/Pictures/'  ''')
            os.system(f'''rclone --config './rclone.conf' move """{filename.replace('.mp4','.png')}"""  'PH_Pics:/Pictures/Caps/'  ''')
            #os.system(f'''rclone --config './rclone.conf' move """{filename}"""  'PH_Pics:/Pictures/'  ''')
            #os.system(f'''rclone --config './rclone.conf' move  """{filename}"""  'Drive:/Backup/'  ''')
            #os.system(f"""rclone --config './rclone.conf' move "Drive:/Backup/" "TD:Backup/" -vP --delete-empty-src-dirs --drive-server-side-across-configs=true """)
            try:
              os.remove(filename.replace(".mp4",".jpg"))
              os.remove(filename.replace(".mp4",".png"))
              os.remove(filename)
            except:
               print("File Moved I guess!!!")     
     #os.system(f'''rclone --config './rclone.conf' copy  """PH_Pictures:/"""  'Drive:/Pictures/'  --drive-server-side-across-configs=true ''')
     #await app.send_message(-1001737315050,f"Update Completed Successfully...", reply_to_message_id=status.id)
     await app.edit_message_text(-1001984459303,4,text=stats("Offline",crtda,count))

app.run(main())
