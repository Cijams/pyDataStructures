class PyQueue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.insert(0, item)

    def deque(self):
        return self.queue.pop() if self.queue else IndexError

    def peek(self):
        return self.queue[-1] if self.queue else IndexError

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return False if self.queue else True

    def clear(self):
        self.queue.clear()
