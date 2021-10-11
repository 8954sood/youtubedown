import asyncio
from youtubedown import asyncDown


async def main():
    Main = await asyncDown.lookup(title="My Songs title or url", path="./music_folder/music") # path = music_folder in music.mp3
    download = await Main.download() #return json and install mp3 file

asyncio.run(main())