# youtubedown


![PYTHON](https://img.shields.io/badge/python-v3.8-blue)
> Asynchronous download using a simple created youtube_dl.

> Required: ffmpeg

> testing python version 3.8



## Asynchronous
```py
import asyncio
from youtubedown import asyncDown


async def main():
    Main = await asyncDown.lookup(title="My Songs title or url", path="./music/music") # path = music polder in music.mp3
    download = await Main.download() #return json and install mp3 file
    search = await Main.search() #retrun json

asyncio.run(main())
```

