class PyHashTable:
    def __init__(self):
        self.table = tuple([] for _ in range(16))
        self.size = 0

    # Adds an element into the hash table.
    def add(self, data):
        try:
            my_hash = self._hash(data)
            if not self.contains(data):
                self.size += 1
                self.table[my_hash].append(data)
        except TypeError as e:
            return e

    # Hash algorithm for picking where to go.
    @staticmethod
    def _hash(data):
        try:
            my_hash = 0
            if type(data) == str or type(data) == chr:
                for _ in data:
                    my_hash = (my_hash + ord(_)) % 293
            elif type(data) == int:
                my_hash = data * 307
            elif type(data) == float:
                my_hash = int((89 + data) // 10)
            else:
                raise AttributeError
            return (~my_hash) * 11 % 16
        except AttributeError as e:
            return e

    # Retrieves the value from the hash table.
    def get(self, data):
        if self.contains(data):
            temp = self.table[self._hash(data)]
            for _ in temp:
                if _ == data:
                    return data

    # Removes the value from the hash table.
    def remove(self, data):
        if self.contains(data):
            temp = self.table[self._hash(data)]
            index = 0
            while index < len(temp):
                if temp[index] == data:
                    del temp[index]
                    self.size -= 1
                    break
                index += 1

    # Removes all data from the hash table.
    def clear(self):
        self.table = tuple([] for _ in range(16))

    # Returns True if the vale is within the hash table.
    def contains(self, data):
        try:
            temp = self.table[self._hash(data)]
            for _ in temp:
                if _ == data:
                    return True
            return False
        except TypeError as e:
            return e

    # Returns the size of the hash table.
    def get_size(self):
        return self.size

    # Returns the hash table
    def get_table(self):
        return self.table
