class pyStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else TypeError

    def peek(self):
        return self.stack[-1] if self.stack else TypeError

    def is_empty(self):
        return False if self.stack else True

    def size(self):
        return len(self.stack)