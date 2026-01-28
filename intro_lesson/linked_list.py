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
            return "Index out of range"

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

    def traverse(self, distance = None):
        if distance == None:
            distance = self._length
        distance -= 1
        curr_node = self._head
        for i in range(distance):
            curr_node = curr_node.next
        return curr_node

    def value_comparison(self, node, target_val, index):
        if node._value == target_val:
            print(f"Value found at index {index}")
            return True
        return False
    
    def search(self, target_val):
        temp_node = self.head
        found = False
        current_index = 0
        
        while current_index <= self.length and not found:
            found = self.value_comparison(temp_node, target_val, current_index)
            temp_node = temp_node.next
            current_index += 1
        
        if not found:
            return "Value not found"
        else:
            return current_index

    def get(self, index):
        return self.traverse(index).value

    def delete_list(self):
        self._head = None

    def pop(self, pop_count = 1):
        if pop_count > self._length:
            return "Index out of range"
        elif pop_count == self._length:
            return self.delete_list()
        
        self.traverse(self._length - pop_count).next = None
        self._length -= pop_count

    def skip(self, node):
        node.next = node.next.next
        if node.next.next == None:
            self._tail = node
        self._length -= 1

    def skipper(self, node, target):
        if type(node.next) == Node and node.next.value == target:
            self.skip(node)

    def delete(self, target_val):
        curr_node = self._head
        while self._head.value == target_val:
            self._head = self._head.next
            self._length -= 1
        for i in range(self._length - 2):
            self.skipper(curr_node, target_val)
            curr_node = curr_node.next


    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @property
    def length(self):
        return self._length
