import asyncio
from youtubedown import asyncDown


async def main():
    Main = await asyncDown.lookup(title="My Songs title or url", path="./music_folder/music", format="mp4") #format list : mp3, wav, mp4, mkv, webm
    download = await Main.download() #return json and install mp3 file

asyncio.run(main())