class PyHashTable:
    def __init__(self):
        self.table = tuple([] for _ in range(16))

    # Adds an element into the hash table.
    def add(self, data):
        self.table[self._hash(data)].append(data)

    # Hash algorithm for picking where to go.
    @staticmethod
    def _hash(data):
        return ~(hash(data) * 11) % 16

    # Retrieves the value from the hash table.
    def get(self):
        pass

    # Removes the value from the hash table.
    def remove(self):
        pass

    # Removes all data from the hash table.
    def clear(self):
        pass

    # Returns an exact copy of the hash table.
    def clone(self):
        pass

    # Returns True if the vale is within the hashtable.
    def contains(self):
        pass

    # Generates a hash code for the given value.
    def hash_code(self):
        pass

    # Returns the size of the hash table.
    def size(self):
        pass

    # Prints the hash table
    def print_table(self):
        print(self.table)
