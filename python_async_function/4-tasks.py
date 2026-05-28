#!/usr/bin/env python3
"""
Task-lar vasitəsilə eyni vaxtda çoxlu korutinlərin işə salınması modulu.
"""
import asyncio
from typing import List

# Tələb olunan funksiyanı 3-tasks.py faylından import edirik
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_random vasitəsilə n sayda task yaradır

    və bitmə sırasına görə delay-ləri qaytarır.
    """
    # task_wait_random artıq birbaşa Task obyekti qaytarır
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
