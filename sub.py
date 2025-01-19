from youtubesearchpython import *
import yt_dlp
import csv,os
import requests
import subprocess
import json
from datetime import timedelta



def duration(filename):
        out = subprocess.check_output(["ffprobe", "-v", "quiet", "-show_format", "-print_format", "json", filename])
        ffprobe_data = json.loads(out)
        duration_seconds = float(ffprobe_data["format"]["duration"])

        td = str(timedelta(seconds=duration_seconds)).split(".")[0]
        return td,str(timedelta(seconds=float(ffprobe_data["format"]["duration"])/2)).split(".")[0]





def gen_sample(filename):
    half = duration(filename)[1]
    output_name = filename.split(".")[0]+"_sample."+filename.split(".")[-1]
    out = subprocess.check_output(["ffmpeg","-i",filename,"-ss",half,"-t","00:00:30","-c:v","copy","-c:a","copy",output_name])
    return output_name





def gettrack(track):
     global token
     URL = "https://api.spotify.com/v1/tracks/" + track + "?access_token=" + token
     r = requests.get(url = URL) 
     data = r.json()
     track = data['name']
     sample= data['preview_url']
     img = data['album']['images'][0]['url']
     return track, sample, img 



def rclone(name,name2):
    rcl = "rclone --config './rclone.conf' copy '" +name+ "' 'Mirror:/Bot/"+ name2 +"'"
    print(rcl)
    os.system(rcl)



def grclone(list,d):
   for name in list:
      if name.endswith(".mp3"):
        gfile = drive.CreateFile({'parents': [{'id': '1lqwn5VB3eBwiCaXwzzcv35LBn-mEKT4H'}]})
        gfile.SetContentFile(d+"/"+name)
        gfile.Upload()


def write(link,name):
  with open("links.csv","a+") as filec:
           cwrite = csv.writer(filec)
           cwrite.writerow([link,name])



def read():
   global cread
   filec = open("links.csv","r")
   cread=csv.reader(filec)
   return cread
 
def ytsq(link):
   tkid=link.split("/")[4].split("?")[0]

   videosSearch = VideosSearch(gettrack(tkid)[0], limit = 1)
   #print(gettrack(tkid)[0])
   #print(videosSearch.result()['result'][0]['link'])
   id = videosSearch.result()['result'][0]['id']
   link = videosSearch.result()['result'][0]['link']
   return id , link

def ytsn(query):
   videosSearch = VideosSearch(query, limit = 1)
   #print(videosSearch.result()['result'])
   id = videosSearch.result()['result'][0]['id']
   link = videosSearch.result()['result'][0]['link']
   title = videosSearch.result()['result'][0]['title']
   img = videosSearch.result()['result'][0]['thumbnails'][0]['url']
   return id , link , title , img 

def dytdl(link):
      ytdl = yt_dlp.YoutubeDL()
      ytdl.download(link)
      info=ytdl.extract_info(link)
      id = info['id']
      return id 

def urlytdl(link):
      ydl_opts = {'format': 'mp4/240/best',
  }
      ytdl = yt_dlp.YoutubeDL(ydl_opts)
      info= ytdl.extract_info(link,download=False)
      return info




def ytdl(link):
   ytlink = [ link ] 
   ydl_opts = {
    'format': 'mp3/bestaudio/best',
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        }]
      }
   with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(ytlink)


def pwrite(link):
  with open("playlist.csv","a+") as filec:
           cwrite = csv.writer(filec)
           cwrite.writerow([link])



def pread():
   global cread
   filec = open("playlist.csv","r")
   cread=csv.reader(filec)
   return cread




def getplay(playlistlink):
     playlist_id = playlistlink[34:].split('?')[0]
     URL = "https://api.spotify.com/v1/playlists/" + playlist_id  + "/tracks?access_token=" + token
     URL2 = "https://api.spotify.com/v1/playlists/"+ playlist_id +"?access_token=" + token  
     r2 = requests.get(URL2)
     pyname = 'Playlist/' + r2.json()['name'] + "'"
     r = requests.get(url = URL) 
     total = r.json()['total']
     count=0
     y=False
     while not y:  
      items = r.json()['items']
      for i in range(len(items)):
         count +=1
         #print(count,r.json()['items'][i]["track"]["external_urls"]["spotify"])
         ytdl(ytsq(r.json()['items'][i]["track"]["external_urls"]["spotify"])[1])
         for name in os.listdir():
           if ytsq(r.json()['items'][i]["track"]["external_urls"]["spotify"])[0] in name:
              rclone(name,pyname)

      else:
         if count ==total:
            y = True
            break
         URL = r.json()['next'] +'&'+ "access_token=" + token
         r = requests.get(url = URL)
     return items




