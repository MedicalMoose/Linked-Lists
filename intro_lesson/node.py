class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    # Shows every node being pointed to from this point
    def __str__(self):
        return (f"Node storing {self._value}, points to {self._next}")

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, new_next):
        self._next = new_next