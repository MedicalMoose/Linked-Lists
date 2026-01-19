from node import Node
from linked_list import LinkedList

new_node = Node(10)
print(new_node)

new_linked_list = LinkedList()
for i in range(10, 31, 10):  # To classmates: third number controls 'step size'
    new_linked_list.append(i)

# Demonstrating append and prepend
new_linked_list.append(40)
new_linked_list.prepend(50)

# Inserts in middle, head, tail, and out of range
new_linked_list.insert(2, 70)
new_linked_list.insert(0, 80)
new_linked_list.insert(8, 90)
new_linked_list.insert(27, 100)

# Debug
print(new_linked_list.head.value)
print(new_linked_list.length)
print(new_linked_list)