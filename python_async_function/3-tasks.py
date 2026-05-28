#!/usr/bin/env python3
"""
Tasks modulu.
"""
import asyncio

# wait_random funksiyasını əvvəlki fayldan import edirik
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """wait_random korutinini qəbul edir və onu asyncio.Task

    obyekti olaraq geri qaytarır.
    """
    return asyncio.create_task(wait_random(max_delay))
