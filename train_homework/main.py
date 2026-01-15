from train import Train

def run_tests():
    t = Train()

    assert t.show() == "None"

    t.add_front(2)
    t.add_front(1)
    t.add_front(0)
    
    assert t.show() == "0 -> 1 -> 2 -> None"
    
    t.add_end(3)
    t.add_end(4)
    
    assert t.show() == "0 -> 1 -> 2 -> 3 -> 4 -> None"
    
    print(t)  # Not part of assignment, debug only
    print(t.show())  # Not part of assignment, debug only
    print("All tests passed!")

run_tests()