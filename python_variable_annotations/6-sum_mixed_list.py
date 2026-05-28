#!/usr/bin/env python3
"""
Qarışıq siyahıdakı ədədləri toplayan modul.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Tam və kəsr ədədlərdən ibarət siyahını toplayır və float qaytarır."""
    return float(sum(mxd_lst))
