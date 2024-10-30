#!/usr/bin/python3
"""Contains the class BasicCache that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """Initialize the cache
        """
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache
        """

        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        """
        return self.cache_data.get(key)
