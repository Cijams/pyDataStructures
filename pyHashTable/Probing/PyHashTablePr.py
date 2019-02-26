class PyHashTablePr:
    def __init__(self):
        self.capacity = 16
        self.table_size = 0
        self.table = tuple([] for _ in range(self.capacity))

    # Adds an element into the hash table.
    def add(self, data):
        try:
            place = self._hash(data)
            if len(self.table[place]) == 0:
                self.table[place].append(data)
                self.table_size += 1
            else:
                self._collision(data, place)
        except TypeError as e:
            return e

    # Finds the next available spot in the table.
    def _collision(self, data, place):
        placing = True
        counter = 0
        while placing:
            place = (place+1) % self.capacity
            if len(self.table[place]) == 0:
                self.table[place].append(data)
                placing = False
            counter = counter+1
            if counter == self.capacity:
                self.resize()
                self.add(data)
                break

    # Resize the table once max capacity is reached.
    def resize(self):
        self.capacity = self.capacity * 2
        temp = self.table
        self.table = tuple([] for _ in range(self.capacity))

        for _ in temp:
            self.add(_[0])

    # Hash algorithm for picking where to go.
    @staticmethod
    def _hash(data):
        try:
            my_hash = 0
            if type(data) == str or type(data) == chr:
                for _ in data:
                    my_hash = (my_hash + ord(_)) % 293
            elif type(data) == int:
                my_hash = data * 307 + 3
            elif type(data) == float:
                my_hash = int((89 + data) // 10)
            else:
                raise AttributeError
            return (~my_hash * 11) % 16
        except AttributeError as e:
            return e

    # Retrieves the value from the hash table.
    def get(self, data):
        return self.table[self._hash(data)] # pick up here

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
        return self.table_size

    # Returns the hash table
    def get_table(self):
        return self.table
