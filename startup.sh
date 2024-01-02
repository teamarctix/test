apt-get update -y && apt-get upgrade -y
wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux
mv yt-dlp_linux yt-dlp
chmod 777 yt-dlp
apt install ffmpeg -y
apt install aria2 -y
pip install pyrogram && pip install tgcrypto && pip install vcsi && pip install moviepy
echo "Package Downloaded and Set"
