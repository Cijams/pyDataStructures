class PySet:
    def __init__(self, head=None):
        self.head = head

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
            print("Duplicate elements not allowed.")

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
