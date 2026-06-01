import asyncio
import random

async def async_generator():
    """A coroutine that yields a random number between 0 and 10, 

    looping 10 times with a 1-second delay between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
