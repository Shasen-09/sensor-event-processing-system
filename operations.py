from data.schemas import Event
from customqueue import CircularQueue
from customarray import CustomArray
from customstack import CustomStack
from data.db import Database


class Operation:
    def __init__(self, queue_capacity, array_capacity, stack_capacity):
        self.queue = CircularQueue(queue_capacity)
        self.array = CustomArray(array_capacity)
        self.stack = CustomStack(stack_capacity)
        self.database = Database()

    def create_event(self, sensor_id, value, timestamp):
        new_event = Event(
            sensor_id=sensor_id,
            value=value,
            timestamp=timestamp
        )
        self.queue.enqueue(new_event)
        return new_event

    def display_events(self):
        return self.queue.display()

    def process_event(self):
        if self.array.is_full():
            raise OverflowError("Recent readings storage is full")
        event = self.queue.dequeue()
        self.array.insert(event.value)
        self.stack.push(event)
        self.database.save_event(event)
        return event

    def current_reading(self):
        return self.array.get_all()

    def recovery_stack(self):
        event = self.stack.pop()
        self.array.delete(self.array.size - 1)
        return event
