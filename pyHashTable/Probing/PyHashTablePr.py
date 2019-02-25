class PyHashTable:
    def __init__(self):
        pass

    # Adds an element into the hash table.
    def add(self, data):
        pass

    # Hash algorithm for picking where to go.
    @staticmethod
    def _hash(data):
        try:
            my_hash = 0
            if type(data) == str or type(data) == chr:
                for _ in data:
                    my_hash = (my_hash + ord(_)) % 512
            elif type(data) == int:
                my_hash = data * 256
            elif type(data) == float:
                my_hash = int((512 + data) // 10)
            else:
                raise AttributeError
            return (~my_hash * 11) % 16
        except AttributeError as e:
            return e

    # Retrieves the value from the hash table.
    def get(self, data):
        pass

    # Removes the value from the hash table.
    def remove(self, data):
        pass

    # Removes all data from the hash table.
    def clear(self):
        self.table = None

    # Returns True if the vale is within the hash table.
    def contains(self, data):
        pass

    # Returns the size of the hash table.
    def get_size(self):
        pass

    # Returns the hash table
    def get_table(self):
        pass
