class PyHashTable:
    def __init__(self):
        self.table = tuple([] for _ in range(16))

    # Adds an element into the hash table.
    def add(self, data):
        try:
            print(self._hash("e"))
            place = self._hash(data)
            print("HASH:" + str(place))
            if len(self.table[place]) == 0:
                self.table[place].append(data)
            else:
                self._collision(data, place)
        except TypeError as e:
            return e

    def _collision(self, data, place):
        print("Collision detected")
        inserted = False
        while inserted:
            place = place+1
            if len(self.table[place] == 0):
                self.table[place].append(data)
                inserted = True

    def resize(self):
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
                my_hash = data * 256 + 3
            elif type(data) == float:
                my_hash = int((512 + data) // 10)
            else:
                raise AttributeError
            return (my_hash) % 16
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
        return self.table
