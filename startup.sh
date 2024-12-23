apt-get update -y && apt-get upgrade -y
wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux
mv yt-dlp_linux yt-dlp
chmod 777 yt-dlp
python3 sibu.py
