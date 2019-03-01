"""
Christopher Ijams 2019
Stack
Linear data structure ordered by last in first out methodology.
"""


class PyStack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        definition = ""
        for e in range(len(self.stack)):
            definition += str(self.stack[e])
            definition += ", "
        return definition[:-2]

    # Push an item onto the stack.
    def push(self, item):
        self.stack.append(item)

    # Remove an element from the stack.
    def pop(self):
        return self.stack.pop() if self.stack else TypeError

    # Returns the next item to be removed.
    def peek(self):
        return self.stack[-1] if self.stack else TypeError

    # Returns True if the stack is empty.
    def is_empty(self):
        return False if self.stack else True

    # Returns the size of the stack.
    def size(self):
        return len(self.stack)

    # Removes all item from the stack.
    def clear(self):
        self.stack.clear()
