#!/usr/bin/env python3
"""
Key-value strukturunu tuple formatına salan modul.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """k mətnini və v-nin kvadratını (float olaraq) tuple daxilində qaytarır."""
    return (k, float(v ** 2))
