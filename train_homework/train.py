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
            

    '''
    Mila asked, so I'll explain here:
    __str__ is basically just a getter that accesses the class as a string
    '''
    def __str__(self):
        temp_carriage = self._head
        result = ''
        while temp_carriage is not None:
            result += str(temp_carriage)
            '''
            Aru asked:
            Yes - we can do if statements in one line
            {command if true} if {condition} else {command if false}
            '''
            result += ", " if temp_carriage.next is not None else ""
            temp_carriage = temp_carriage.next
        return result

    '''
    Not a fan of how this was structured, but :P
    Show is basically just acting like a secondary __str__
    '''
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
        # Gets done anyway, no need for else 
        new_carriage.next = self._head
        self._head = new_carriage
        self._length += 1

    # How I WOULD do it
    def add_end_o1(self, number):
        new_carriage = Carriage(number)
        if self._head is None:
            self._head = new_carriage
        else:
            self._tail.next = new_carriage
        self._tail = new_carriage
        self._length += 1

    # How we HAD to do it, hated this method
    def add_end(self, number):
        # I hate that this method is now on my Github
        current_node = self._head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Carriage(number)
        self._tail = current_node.next
        self._length += 1