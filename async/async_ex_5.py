import asyncio
import time


async def task_1():
    print("Zadanie 1 rozpoczęte...")
    await asyncio.sleep(4)
    print("Zadanie 1 zakończone")


async def task_2():
    print("Zadanie 2 rozpoczete...")
    await asyncio.sleep(1)
    print("Zadanie 2 zakończone")


async def task_3():
    print("Zadanie 3 rozpoczęte...\n")
    await asyncio.sleep(2)
    print("Zadanie 3 zakończone")


async def main():
    start_time = time.time()
    await asyncio.gather(task_1(), task_2(), task_3())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("\nWszystkie zadania zakończyły się w ciągu {:.2f} sekund".format(elapsed_time))


asyncio.run(main())
