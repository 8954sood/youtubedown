from youtubedown import asyncDown
import asyncio

async def main():
    classd = await asyncDown.lookup(title="https://www.youtube.com/watch?v=09R8_2nJtjg",format='wav' , path='music', debug=True)
    data = await classd.download()
    # with open('data.txt', 'w', encoding='utf-8') as E:
    #     E.write(f"{data}")
    
    print(data)
    

asyncio.run(main())