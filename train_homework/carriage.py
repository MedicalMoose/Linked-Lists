class Carriage:
    def __init__(self, number):
        self._number = number
        self._next = None

    def __str__(self):
        return f"Carriage No. {self._number}"

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, new_number):
        self._number = new_number
    
    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_carriage):
        self._next = next_carriage
