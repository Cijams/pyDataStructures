"""
Christopher Ijams
Set
Unordered collection of objects with no duplicates.
"""


class PySet:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        curr = self.head
        definition = ""
        while curr:
            definition += str(curr.data) + ", "
            curr = curr.next
        return "{" + definition[:-2] + "}"

    # Add two sets together - Union
    def __add__(self, set_one):
        try:
            temp = self.iterate()
            my_set = set()
            for _ in temp:
                my_set.add(_)
            for _ in set_one.iterate():
                my_set.add(_)
            return my_set
        except TypeError as e:
            return e

    # Returns true if both sets are of equal size.
    def __eq__(self, other):
        try:
            my_set = self.iterate()
            other_set = other.iterate()
            return True if self.size(my_set) == self.size(other_set) else False
        except TypeError as e:
            return e

    # Returns True if the first set is larger than the second.
    def __gt__(self, other):
        try:
            my_set = self.iterate()
            other_set = other.iterate()
            return True if self.size(my_set) > self.size(other_set) else False
        except TypeError as e:
            return e

    # Returns True if the first set is smaller than the second.
    def __lt__(self, other):
        try:
            my_set = self.iterate()
            other_set = other.iterate()
            return True if self.size(my_set) < self.size(other_set) else False
        except TypeError as e:
            return e

    # Returns the size of the set
    @staticmethod
    def size(curr):
        count = 0
        try:
            for _ in curr:
                count += 1
            return count
        except TypeError:
            return "Pass the head of the set."

    # Adds an element to the set.
    def add(self, data=None):
        if not self.contains(data):
            curr_node = self._Node(data)
            curr_node.next = self.head
            self.head = curr_node

    # Returns True if the set contains the data.
    def contains(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    # Remove an element from the set.
    def remove(self, data):
        curr = self.head
        try:
            if curr.data == data:
                self.head = curr.next
                return True
            while curr:
                if curr.next.data == data:
                    curr.next = curr.next.next
                    return True
                curr = curr.next
        except AttributeError:
            return False

    # Returns the set
    def iterate(self):
        return_set = set()
        curr = self.head
        while curr:
            return_set.add(curr.data)
            curr = curr.next
        return return_set

    # Finds an element in the set and alters the value.
    def change(self, data, mod):
        curr = self.head
        try:
            while curr:
                if curr.data == data:
                    if self.contains(mod):
                        raise AttributeError
                    else:
                        curr.data = mod
                        break
                curr = curr.next
        except AttributeError:
            return "Duplicate elements not allowed."

    # Returns the length of the set.
    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    # Clears the set.
    def clear(self):
        self.head = None

    # Removes the last element from the set.
    def pop(self):
        curr = self.head
        if curr:
            if curr.next is None:
                self.head = None
            while curr.next.next:
                curr = curr.next
            curr.next = None

    # Returns a set containing the difference between two sets
    @staticmethod
    def difference(set_one, set_two):
        try:
            my_map = {}
            my_map = PySet._counter(set_one, my_map)
            my_map = PySet._counter(set_two, my_map)
            return_set = set()
            for _ in my_map:
                if my_map.get(_) == 1:
                    return_set.add(_)
            return return_set
        except AttributeError as e:
            print(e)

    # Returns a set that is the intersection of two sets.
    @staticmethod
    def intersection(set_one, set_two):
        try:
            my_map = {}
            my_map = PySet._counter(set_one, my_map)
            my_map = PySet._counter(set_two, my_map)
            return_set = set()
            for _ in my_map:
                if my_map.get(_) > 1:
                    return_set.add(_)
            return return_set
        except AttributeError as e:
            print(e)

    # Returns whether two sets have an intersection.
    @staticmethod
    def is_disjoint(set_one, set_two):
        try:
            my_map = {}
            my_map = PySet._counter(set_one, my_map)
            my_map = PySet._counter(set_two, my_map)
            for _ in my_map:
                if my_map.get(_) > 1:
                    return False
            return True
        except AttributeError as e:
            print(e)

    # Returns true if the first set is a subset of the second.
    @staticmethod
    def is_subset(set_one, set_two):
        try:
            for _ in set_one.iterate():
                if _ not in set_two.iterate():
                    return False
            return True
        except AttributeError as e:
            print(e)

    # Returns a set that is the union of two sets.
    @staticmethod
    def union(set_one, set_two):
        try:
            my_set = set()
            for _ in set_one.iterate():
                my_set.add(_)
            for _ in set_two.iterate():
                my_set.add(_)
            return my_set
        except AttributeError as e:
            print(e)

    # Helper methods to count the occurrences of each element
    @staticmethod
    def _counter(set_one, my_map):
        my_list = set_one.iterate()
        for i in my_list:
            if my_map.get(i) is None:
                my_map[i] = 1
            else:
                my_map[i] = my_map.get(i) + 1
        return my_map

    # Node class for linking and data storage.
    class _Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
