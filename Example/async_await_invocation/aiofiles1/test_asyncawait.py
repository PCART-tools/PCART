import aiofiles
import asyncio

async def async_file_io():
    async with aiofiles.open('test.txt', mode='w') as f:
        await f.write('Hello, world!')
    
    async with aiofiles.open('test.txt', mode='r') as f:
        content = await f.read()
    return content

# run
data = asyncio.run(async_file_io())
