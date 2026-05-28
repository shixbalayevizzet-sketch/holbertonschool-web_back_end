import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """0 ilə max_delay arasında təsadüfi bir müddət gözləyir

    və həmin müddəti (saniyəni) geri qaytarır.
    """
    # random.uniform() 0 ilə max_delay arasında təsadüfi bir float (kəsr) ədəd seçir
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
