#!/usr/bin/env python3
"""
Server modulu, məlumat bazasının səhifələnməsi üçün istifadə olunur.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Verilmiş səhifə və səhifə ölçüsü üçün başlanğıc və son indeksləri hesablayır.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Səhifə nömrəsinə və ölçüsünə görə məlumatı qaytarır.

        Args:
            page (int): Səhifə nömrəsi.
            page_size (int): Hər səhifədəki sətir sayı.

        Returns:
            List[List]: Səhifələnmiş məlumatlar siyahısı.
        """
        # Argumanların tam ədəd və sıfırdan böyük olduğunu yoxlayırıq
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Məlumat bazasını əldə edirik
        dataset = self.dataset()

        # index_range funksiyasından istifadə edərək indeksləri alırıq
        start, end = index_range(page, page_size)

        # Əgər indekslər dataset-in uzunluğundan böyükdürsə, boş siyahı qaytarırıq
        if start >= len(dataset):
            return []

        # Dilimlənmiş məlumatı qaytarırıq
        return dataset[start:end]
