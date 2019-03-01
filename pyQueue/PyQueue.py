"""
Christopher Ijams
Queue
Linear data structure ordered by first in first out methodology.
"""


class PyQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        definition = ""
        for e in range(len(self.queue)):
            definition += str(self.queue[e])
            definition += ", "
        return definition[:-2]

    # Push an item onto the queue.
    def push(self, item):
        self.queue.insert(0, item)

    # Remove an element from the queue.
    def deque(self):
        return self.queue.pop() if self.queue else IndexError

    # Returns the next item to be removed.
    def peek(self):
        return self.queue[-1] if self.queue else IndexError

    # Returns the size of the queue.
    def size(self):
        return len(self.queue)

    # Returns True if the queue is empty.
    def is_empty(self):
        return False if self.queue else True

    # Removes all item from the queue.
    def clear(self):
        self.queue.clear()
