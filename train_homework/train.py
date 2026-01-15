# https://music.youtube.com/watch?v=qthko5ppHcM&list=TLGGu7v7fGQFQgkwODAxMjAyNg
from carriage import Carriage

class Train:
    ''' 
    To students: *cars is our args statement here
    Args are tuples that store as much data as we give
    This allows us to handle 0, 1, and many starting cars more simply
    '''
    def __init__(self, *cars):  
        self._head = None
        self._tail = None
        self._length = 0
        for car in cars:
            self.add_end(car)
            
    def __str__(self):
        temp_carriage = self._head
        result = ''
        while temp_carriage is not None:
            result += str(temp_carriage)
            result += ", " if temp_carriage.next is not None else ""
            temp_carriage = temp_carriage.next
        return result

    def show(self):
        temp_carriage = self._head
        result = ''
        while temp_carriage is not None:
            result += str(temp_carriage.number)
            result += " -> "
            temp_carriage = temp_carriage.next
        result += "None"
        return result

    def count(self):
        return self._length

    def add_front(self, number):
        new_carriage = Carriage(number)
        if self._tail is None:
            self._tail = new_carriage
        new_carriage.next = self._head
        self._head = new_carriage
        self._length += 1

    def add_end_o1(self, number):
        new_carriage = Carriage(number)
        if self._head is None:
            self._head = new_carriage
        else:
            self._tail.next = new_carriage
        self._tail = new_carriage
        self._length += 1

    def add_end(self, number):
        # This method is why I'm not uploading this to Github
        current_node = self._head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Carriage(number)
        self._tail = current_node.next
        self._length += 1
