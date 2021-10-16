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
    Main = await asyncDown.lookup(title="My Songs title or url", path="./music_folder/music", format="mp3") # path = music_folder in music.mp3
    download = await Main.download() #return json and install mp3 file

asyncio.run(main())
```

Examples of source codes can be found through ["Click"](https://github.com/8954sood/youtubedown/tree/main/example).

An example of a return value can be found through ["Click"](https://github.com/8954sood/youtubedown/blob/main/example/return.json).
