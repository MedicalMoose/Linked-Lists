from node import Node

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0


    def __str__(self):
        temp_node = self._head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '  # Done for aesthetics only
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
        if self._tail is None:
            self._tail = new_node
        new_node.next = self._head  # Outside the if statement because we'll always do it
        self._head = new_node
        self._length += 1


new_linked_list = LinkedList()
for i in range(10, 31, 10):  # To classmates: third number controls 'step size'
    new_linked_list.append(i)
new_linked_list.append(40)
new_linked_list.prepend(50)

print(new_linked_list._head.value)
print(new_linked_list._length)
print(new_linked_list)
