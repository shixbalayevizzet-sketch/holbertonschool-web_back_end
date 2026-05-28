import asyncio
import time

# Əgər əvvəlki faylınızın adı, məsələn, "fayl_adi.py" idisə, oradan import edirik:
# (Burada şərti olaraq "script" yazılıb, öz faylınızın adını qeyd edə bilərsiniz)
from script import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """wait_n(n, max_delay) funksiyasının ümumi icra vaxtını ölçür

    və orta icra vaxtını (total_time / n) float olaraq qaytarır.
    """
    # Başlanğıc vaxtı qeyd edirik
    start_time = time.time()

    # Asinxron wait_n funksiyasını burada işə salırıq
    asyncio.run(wait_n(n, max_delay))

    # Bitiş vaxtını qeyd edirik
    end_time = time.time()

    # Ümumi keçən vaxtı hesablayırıq
    total_time = end_time - start_time

    # n-ə bölərək orta göstəricini qaytarırıq
    return total_time / n
