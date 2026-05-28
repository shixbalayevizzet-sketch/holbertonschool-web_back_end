#!/usr/bin/env python3
"""
Multipliers yaradan modul.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplier arqumentinə əsasən funksiya yaradır və qaytarır."""
    def multiplier_function(number: float) -> float:
        """Daxil edilən ədədi əsas multiplier-a vurur."""
        return number * multiplier

    return multiplier_function
