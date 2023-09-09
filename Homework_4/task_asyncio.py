import asyncio

import aiofiles
import aiohttp
import time

urls = ['https://gb.ru/_nuxt/img/89f1beb.png',
        'https://photocentra.ru/images/main78/781689_main.jpg',
        'https://gb.ru/_nuxt/img/6c757d5.png',
        'https://gb.ru/_nuxt/img/6cc126e.png',
        'https://gb.ru/_nuxt/img/6c83daa.png']

# urls = sys.argv


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            filename = 'pars/' + url.split('/')[-1]
        with open(filename, "wb") as f:
            f.write(content)
        print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    asyncio.run(main())

print(f"Total download time {time.time() - start_time: .2f} seconds")