import asyncio


async def display_with_delay(name, delay):
    await asyncio.sleep(delay)
    print(name)


async def main():
    tasks = [
        display_with_delay("Funkcja asynchroniczna nr 1", 1),
        display_with_delay("Funkcja asynchroniczna nr 2", 2),
        display_with_delay("Funkcja asynchroniczna nr 3", 3),
    ]

    await asyncio.gather(*tasks)

asyncio.run(main())
