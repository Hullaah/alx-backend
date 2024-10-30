#!/usr/bin/python3
"""Contains the  class LIFOCache that inherits from BaseCaching
 and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self) -> None:
        """Initialize the cache
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item to the cache
        """

        if key is None or item is None:
            return

        if (key not in self.cache_data and
                len(self.cache_data) == self.MAX_ITEMS):
            discarded_item = self.stack[-1]

            print("DISCARD:", discarded_item)

            self.stack = self.stack[:-1]

            while True:
                try:
                    del self.cache_data[discarded_item]
                    break
                except KeyError:
                    discarded_item = self.stack[-1]
                    self.stack = self.stack[:-1]

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """Get an item by key
        """
        return self.cache_data.get(key)
