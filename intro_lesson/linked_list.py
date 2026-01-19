from node import Node

class LinkedList:
    def __init__(self, *values):
        self._head = None
        self._tail = None
        self._length = 0
        for value in values:
            self.append(value)

    def __str__(self):
        temp_node = self._head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            result += " -> " if temp_node.next is not None else ""
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self._head is None:
            self._tail = new_node
        new_node.next = self._head  # Outside the if statement because we'll always do it
        self._head = new_node
        self._length += 1

    def insert(self, index, value):
        temp_node = self._head

        # Prevents inserting at an index we can't access
        if index > self._length:
            print("Index out of range")
            return

        # If inserting at the head position: prepend
        elif index == 0:
            return self.prepend(value)

        # If inserting at the tail position: append
        elif index == self._length:
            return self.append(value)

        # If insering in the middle: traverse then insert at index
        new_node = Node(value)
        for i in range(index - 1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self._length += 1

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @property
    def length(self):
        return self._length
