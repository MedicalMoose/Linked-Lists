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

    def skip(self, node):
        # Sets to the next next node, rather than the next node
        node.next = node.next.next

        # If there's no next next node, the current node is now the tail
        if node.next.next == None:
            self._tail = node
        self._length -= 1

    """
    This method exists to avoid nesting, watch this video to get why
    https://www.youtube.com/watch?v=CFRhGnuXG-4
    """
    def skipper(self, node, target):
        # This is done for the delete() method later on
        if type(node.next) == Node and node.next.value == target:
            self.skip(node)

    def append(self, value):
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
        else:
            #This is so we don't accidentally try to give None a tail
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
            raise IndexError  # Creates an error, halting the program

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

    # We specify how many nodes deep we want to go, and return the node at that index
    def traverse(self, distance = None):  # "distance = None" gives distance a default value
        # Sets the default index to the tail, and avoids out-of-range errors 
        if distance == None or distance >= self.length:
            distance = self._length - 1
        
        # Allows us to feign reverse indexing
        elif distance < 0:
            distance += self._length
        
        # Starting at the head lets us take 0 as an index
        curr_node = self._head
        for i in range(distance):
            curr_node = curr_node.next
        return curr_node

    def value_comparison(self, node, target_val, index):
        # This is for the search() method just below
        if node._value == target_val:
            # Gives us the index of the data we were looking for
            print(f"{target_val} found at index {index}")
            return True
        return False
    
    # Seeks a target, and returns its location in the list
    def search(self, target_val):
        temp_node = self.head
        found = False
        current_index = 0
        
        # Thid lets us catch multiple instances of target_val in the list
        while current_index < self.length:
            found = self.value_comparison(temp_node, target_val, current_index)
            temp_node = temp_node.next
            current_index += 1
        
        if not found:
            return None
        else:
            return current_index

    def get(self, index):
        if index > -1 and index < self._length:
            # We want to return a node, not an integer
            return self.traverse(index)
        else:
            raise IndexError
        
    def set(self, index, new_value):
        # Uses the get() method, as a validation check is already there
        self.get(index).value = new_value

    def delete_list(self):
        self._head = None

    def pop_start(self, pop_count = 1):
        if pop_count > self._length:
            raise IndexError
        elif pop_count == self._length:
            return self.delete_list()
        
        # Traverses a number of nodes, and makes the destination the new head
        self._head = self.traverse(pop_count)
        self._length -= pop_count

    def pop_end(self, pop_count = 1):
        if pop_count > self._length:
            raise IndexError
        elif pop_count == self._length:
            return self.delete_list()
        
        # Don't forget to reassign the tail - I forgot!
        self._tail = self.traverse(self._length - pop_count - 1)
        self.traverse(self._length - pop_count - 1).next = None
        self._length -= pop_count

    # Overcomplicated, did it for fun :P
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
