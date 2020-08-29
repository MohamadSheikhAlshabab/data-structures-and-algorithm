from data_structures_and_algorithm.Data_Structures.linked_list import LinkedList,Node


def test_empty_list():
    ll = LinkedList()
    assert ll.head == None

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

def test_k_is_negative():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    actual = ll.kth_from_end(-1)
    expected = '-1 is not in the range of the list'
    assert expected == actual

def test_list_length_is_one():
    ll = LinkedList()
    ll.insert(1)
    actual = ll.kth_from_end(0)
    expected = 1
    assert expected == actual

def test_happy_path():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)
    actual = ll.kth_from_end(3)
    expected =3

    assert expected == actual