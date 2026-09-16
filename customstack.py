class CustomStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top + 1 == self.capacity

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.top += 1
        self.stack[self.top] = value

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        value = self.stack[self.top]
        return value

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        value = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return value
