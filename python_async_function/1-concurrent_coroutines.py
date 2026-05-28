#!/usr/bin/env python3
"""
Eyni vaxtda çoxlu korutinlərin işə salınması modulu.
"""
import asyncio
from typing import List

# Düzgün import forması budur:
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_random korutinini n dəfə eyni vaxtda çağırır

    və bitmə sırasına görə delay-ləri qaytarır.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
