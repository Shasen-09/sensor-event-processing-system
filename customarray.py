class CustomArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def insert(self, value):
        if self.is_full():
            print("Array is full")
            return

        self.array[self.size] = value
        self.size += 1

    def traversal(self):
        for i in range(self.size):
            print(self.array[i])
        print()

    def get_all(self):
        return self.array[:self.size]

    def get_item(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Array out of range")
        return self.array[index]

    def set_item(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Array out of range")
        self.array[index] = value

    def search(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Array out of range")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i+1]
        self.array[self.size-1] = None
        self.size -= 1
