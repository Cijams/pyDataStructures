"""
Christopher Ijams
Deque
A linear generalization of stack and queue functionality combined.
"""


class PyDeque:

    def __init__(self, max_length=0):
        self.deque = []
        self.limited = False
        if max_length > 0:
            self.max_length = max_length
            self.limited = True

    # Return a string representing the deque.
    def __str__(self):
        return str(self.deque)

    # Adds an element into the deque.
    def append(self, data):
        try:
            if self.limited:
                if self.count() < self.max_length:
                    self.deque.append(data)
                else:
                    raise DequeFull
            else:
                self.deque.append(data)
        except DequeFull as e:
            return e

    # Adds en element into the deque on the left.
    def append_left(self, data):
        if self.limited:
            if self.count() < self.max_length:
                self.deque.reverse()
                self.append(data)
                self.deque.reverse()
        else:
            self.deque.reverse()
            self.append(data)
            self.deque.reverse()

    # Clears the deque of all values.
    def clear(self):
        self.deque = []

    # Returns an integer representing the length of the deque.
    def count(self):
        return len(self.deque)

    # Removes the right most element from the deque.
    def pop(self):
        try:
            self.deque.pop()
        except IndexError as e:
            return e

    # Removes the left most element from the deque.
    def pop_left(self):
        try:
            self.deque.reverse()
            self.deque.pop()
            self.deque.reverse()
        except IndexError as e:
            return e

    # Rotates the deque by a specified amount left.
    def rotate(self, rotations):
        self.deque = self.deque[rotations:] + self.deque[:rotations]

    # Extends the size limit of the deque
    def extend(self, size):
        if type(size) is int:
            if self.limited:
                self.max_length += size
        else:
            return "extend only accepts an integer"

    # Reverses the elements in the deque
    def reverse(self):
        self.deque.reverse()

    # Sets the maximum length of the deque
    def max_len(self, length):
        if type(length) is not int:
            raise TypeError
        if self.limited:
            if self.max_length < length:
                self.max_length = length
            else:
                temp_deque = []
                for e in range(length):
                    temp_deque.append(self.deque[e])
                self.deque = temp_deque


# Raised when user tries to add to many elements into a limited Deque
class DequeFull(Exception):
    Message = "Deque is at capacity"
