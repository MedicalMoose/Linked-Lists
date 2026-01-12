from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    
    def prepend(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1


new_linked_list = LinkedList()
for i in range(10, 21):
    new_linked_list.append(i)
new_linked_list.append(21)
new_linked_list.prepend(9)

print(new_linked_list.head.value)
print(new_linked_list.length)
print(new_linked_list)
