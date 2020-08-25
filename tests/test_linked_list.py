from data_structures_and_algorithm.linked_list.linked_list import ( LinkedList,Node,)

def test_kth_from_end_2():
    list1 = LinkedList()
    list1.append('1')
    list1.append('2')
    list1.append('3')
    assert list1.kth_from_end(1) == '2'

def test_kth_from_end_1():
    list1 = LinkedList()
    list1.append('1')
    list1.append('2')
    list1.append('3')
    assert list1.kth_from_end(0) == '1'

def test_reverse_1():
    list1 = LinkedList()
    list1.append('1')
    list1.append('2')
    list1.append('3')
    assert list1.reverse() == '1'

def test_reverse_2():
    list1 = LinkedList()
    list1.append('1')
    list1.append('2')
    list1.append('3')
    assert list1.reverse() == '3'

def test_reverse_3():
    list1 = LinkedList()
    list1.append('1')
    list1.append('2')
    list1.append('3')
    assert list1.reverse() == '2'

def test_kth_from_end_3():
    list1 = LinkedList()
    list1.append('1')
    list1.append('2')
    list1.append('3')
    assert list1.kth_from_end(2) == '3'