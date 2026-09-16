class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear+1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        value = self.queue[self.front]
        self.queue[self.front] = None
        self.size -= 1

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front+1) % self.capacity
        return value

    def display(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        events = []
        i = self.front
        while True:
            events.append(self.queue[i])

            if i == self.rear:
                break
            i = (i+1) % self.capacity
        return events

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.queue[self.front]
        return value
