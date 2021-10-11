import asyncio
from youtubedown import asyncDown


async def main():
    YDL_OPTIONS = {
    'format': 'bestaudio/best',
    'quiet': True,
    'outtmpl': 'mymsuic.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
    }
    Main = await asyncDown.lookup(title="My Songs title or url", option=YDL_OPTIONS) # path = music polder in music.mp3
    download = await Main.download() #return json and install mp3 file

asyncio.run(main())