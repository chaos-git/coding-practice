'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.newest = None
        self.oldest = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        value = self.cache[key].value
        self.put(key, value)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.__pop(key)

        if len(self.cache) == self.capacity:
            self.__pop(self.oldest.key)

        # put on top of our doubly linked list (it's the newest item)
        node = Node(key, value)
        if self.newest:
            node.next = self.newest
            self.newest.prev = node
        self.newest = node
        if not self.oldest:
            self.oldest = self.newest
        self.cache[key] = node

    def __pop(self, key):
        node = self.cache[key]

        if node.prev:  #  if not newest
            node.prev.next = node.next
        else:
            self.newest = node.next

        if node.next:  # if not oldest
            node.next.prev = node.prev
        else:
            self.oldest = node.prev

        del self.cache[key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
