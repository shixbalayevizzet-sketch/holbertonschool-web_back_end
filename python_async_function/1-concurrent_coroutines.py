import asyncio
from typing import List

# Əgər əvvəlki faylın adı "script.py" idisə, ondan import edirik:
from script import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_random korutinini n dəfə eyni vaxtda (concurrency) çağırır

     və bitmə ardıcıllığına görə (artan sıra ilə) delay-ləri qaytarır.
    """
    # n sayda wait_random tapşırığı yaradırıq
    tasks = [wait_random(max_delay) for _ in range(n)]

    delays = []

    # as_completed hansı task birinci bitsə, onu dərhal yield edir
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
