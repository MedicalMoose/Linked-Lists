from node import Node
from linked_list import LinkedList

new_node = Node(10)
print(new_node)

empty_linked_list = LinkedList()
new_linked_list = LinkedList()
for i in range(10, 31, 10):  # To classmates: third number controls 'step size'
    new_linked_list.append(i)

# Demonstrating append and prepend
new_linked_list.append(40)
new_linked_list.prepend(50)

# Inserts in middle, head, tail, and out of range
new_linked_list.insert(2, 70)
new_linked_list.insert(0, 80)
# new_linked_list.insert(8, 90)
# new_linked_list.insert(27, 100)
new_linked_list.insert(3, 50)
new_linked_list.prepend(50)


# Tests
def run_tests():
    l_l = LinkedList()

    assert str(l_l) == ""

    l_l.append(20)
    l_l.prepend(10)
    l_l.prepend(0)

    assert str(l_l) == "0 -> 10 -> 20"

    l_l.append(30)
    l_l.insert(4, 40)

    assert str(l_l) == "0 -> 10 -> 20 -> 30 -> 40"

    print("All tests passed!")

if __name__ == "__main__":
    # Printing different values
    print(new_linked_list.head.value)
    print(new_linked_list.length)
    print(new_linked_list)
    new_linked_list.search(50)
    new_linked_list.pop_end(2)
    new_linked_list.pop_start()
    new_linked_list.prepend(60)
    new_linked_list.delete(50)
    new_linked_list.set(2, 90)
    print(new_linked_list)
    print(new_linked_list.length)
    print()
    run_tests()
    print()
    new_linked_list.traverse()
    print()
    empty_linked_list.traverse()