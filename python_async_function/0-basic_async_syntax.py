#!/usr/bin/env python3
"""
Maksimum gecikmə ilə təsadüfi gözləmə modulu.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """0 ilə max_delay arasında təsadüfi saniyə gözləyir və qaytarır."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
