class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dispaly(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("NULL")

    def delete_from_begining(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail


mylist = LinkedList()

mylist.insert_at_beginning(10)
mylist.insert_at_beginning(20)
mylist.insert_at_beginning(30)
mylist.insert_at_end(40)
mylist.delete_from_begining()
mylist.dispaly()
