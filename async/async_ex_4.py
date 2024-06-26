import asyncio
import aiohttp


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url_1 = "https://www.wikipedia.org/"
    url_2 = "https://www.google.com"
    task_1 = asyncio.create_task(fetch_url(url_1))
    task_2 = asyncio.create_task(fetch_url(url_2))
    data_1 = await task_1
    data_2 = await task_2
    print(f"Dane z {url_1} {len(data_1)} bajtów")
    print(f"Dane z {url_2} {len(data_2)} bajtów")


asyncio.run(main())
