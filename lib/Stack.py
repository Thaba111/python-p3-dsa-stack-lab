class Stack:
    def __init__(self, items=None, limit=None):
        self.items = items if items is not None else []
        self.limit = limit

    def push(self, item):
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise ValueError("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        pass
    
    def search(self, value):
        for i, item in enumerate(reversed(self.items)):
            if item == value:
                return i
        return -1
