#!/usr/bin/env python3
"""
This module provides a Server class to paginate a database of popular baby names.
"""
import csv
from typing import List

# Funksiyanı digər fayldan idxal edirik
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server instance with an empty dataset.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and return the cached dataset from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset based on pagination parameters.

        Args:
            page (int): The page number to retrieve (1-indexed).
            page_size (int): The number of items to include in the page.

        Returns:
            List[List]: The list of rows corresponding to the requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]
