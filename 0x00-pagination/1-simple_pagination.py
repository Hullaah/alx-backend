#!/usr/bin/env python3
"""Implements a simple pagination
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """A function that takes two integer arguments page and page_size and
    return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return
    in a list for those particular pagination parameters
    """
    return ((page * page_size) - page_size, page * page_size)


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
        """Gets pages from a dataset
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        (start, stop) = index_range(page, page_size)
        return self.dataset()[start:stop]
