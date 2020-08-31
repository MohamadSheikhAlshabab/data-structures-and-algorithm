from data_structures_and_algorithm.linked_list.linked_list import LinkedList,Node


def test_empty_list():
    ll = LinkedList()
    assert ll.head == None

# def test_head():
#     ll = LinkedList()
#     ll.append_value(5)
#     ll.append_value(10)
#     assert ll.head == 5

def test_insert_to_empty_ll():
    ll = LinkedList()
    ll.insert(5)
    assert ll.head.value == 5

def test_multiple_insert():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    ll.insert(7)
    assert ll.to_string() == 'head-> {5}->{6}->{7}->NULL'

def test_includes():
    ll = LinkedList()
    ll.insert(5)
    ll.append_value(55)
    assert ll.includes(5) == True

def test_includes_false():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(77)
    ll.insert(75)
    assert ll.includes(6) == False

def test_dender_str():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    ll.insert(7)
    assert ll.to_string() == 'head-> {5}->{6}->{7}->NULL'

def test_insert_before():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    ll.insert(8)
    ll.insert(9)
    ll.insert_before(6,7)
    assert ll.to_string() == 'head-> {5}->{7}->{6}->{8}->{9}->NULL'

def test_insert_after():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    ll.insert(8)
    ll.insert(9)
    ll.insert_after(8,7)
    assert ll.to_string() == 'head-> {5}->{6}->{8}->{7}->{9}->NULL'
