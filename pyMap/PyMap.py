"""
Christopher Ijams
Map
Associative container storing key value pairs.
"""


class PyMap:
    def __init__(self):
        self.head = None

    def __str__(self):
        hm = ""
        curr = self.head
        while curr:
            hm += "{" + str(curr.key) + ": " + str(curr.value) + "}, "
            curr = curr.next
        return hm[:-2]

    # Add a key-value pair into the map.
    def put(self, key=None, value=None):
        if self.head:
            if self.retrieve(key):
                curr = self.retrieve(key)
                curr.value = value
            else:
                curr = self._Node(key, value)
                curr.next = self.head
                self.head = curr
        else:
            self.head = self._Node(key, value)

    # Returns a list of the keys in the map.
    def keys(self):
        curr = self.head
        keys = []
        while curr:
            keys.append(curr.key)
            curr = curr.next
        return keys

    # Returns a list of the values in the map.
    def values(self):
        curr = self.head
        values = []
        while curr:
            values.append(curr.value)
            curr = curr.next
        return values

    # Removes the last key-value pair in the map.
    def pop(self):
        if self.head.next is None:
            self.head = None
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None

    # Returns the position of the key-value pair
    def retrieve(self, key):
        if self.head.key == key:
            return self.head
        else:
            curr = self.head
            while curr.next:
                if curr.next.key == key:
                    return curr.next
                else:
                    curr = curr.next
        return False

    # Returns True if the map contains the key
    def contains_key(self, key):
        if self.head.key == key:
            return True
        else:
            curr = self.head
            while curr.next:
                if curr.next.key == key:
                    return True
                else:
                    curr = curr.next
        return False

    # Returns True if the map contains the value
    def contains_value(self, value):
        if self.head.value == value:
            return True
        else:
            curr = self.head
            while curr.next:
                if curr.next.value == value:
                    return True
                else:
                    curr = curr.next
        return False

    # Removes a value and key from the map with the given key.
    def remove_key(self, key):
        if self.head.key == key:
            self.head = self.head.next
        else:
            curr = self.head
            while curr.next:
                if curr.next.key == key:
                    curr.next = curr.next.next
                    return True
                else:
                    curr = curr.next
        return False

    # Internal node class to store key-value pairs.
    class _Node:
        def __init__(self, key=None, value=None):
            self.next = None
            self.key = key
            self.value = value

