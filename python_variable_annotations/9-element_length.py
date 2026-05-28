#!/usr/bin/env python3
"""
Siyahının elementlərinin uzunluğunu hesablayan modul.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Hər bir elementin özünü və uzunluğunu ehtiva edən tuple-lar siyahısı

    qaytarır.
    """
    return [(i, len(i)) for i in lst]
