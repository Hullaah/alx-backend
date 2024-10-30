#!/usr/bin/python3
"""Contains the  class MRUCache that inherits from BaseCaching
 and is a caching system
"""
from base_caching import BaseCaching
from datetime import datetime


class MRUCache(BaseCaching):
    """MRUCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self) -> None:
        """Initialize the cache
        """
        super().__init__()
        self.recency_store = {}

    def put(self, key, item):
        """Add an item to the cache
        """

        if key is None or item is None:
            return

        if (key not in self.cache_data and
                len(self.cache_data) == self.MAX_ITEMS):
            discarded_item, _ = max(
                self.recency_store.items(),
                key=lambda x: x[1]
            )

            print("DISCARD:", discarded_item)

            del self.recency_store[discarded_item]
            del self.cache_data[discarded_item]

        self.cache_data[key] = item
        self.recency_store[key] = datetime.now()

    def get(self, key):
        """Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.recency_store[key] = datetime.now()
        return self.cache_data.get(key)
