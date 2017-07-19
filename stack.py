class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items():
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None
