#!/usr/bin/env python3
"""
Multipliers (vuranlar) yaradan modul.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Arqument kimi verilən multiplier-a əsasən yeni vurma funksiyası

    yaradır və həmin funksiyanı geri qaytarır.
    """
    def multiplier_function(number: float) -> float:
        """Daxil edilən ədədi əsas multiplier-a vurur."""
        return number * multiplier

    return multiplier_function
