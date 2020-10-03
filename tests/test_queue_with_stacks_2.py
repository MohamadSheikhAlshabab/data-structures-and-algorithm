from data_structures_and_algorithm.challenge.queue_with_stacks.queue_with_stacks_2 import Pseudo_Queue,Stack,Node
import pytest

def test_Happy_Path_enqueue():
    queue = Pseudo_Queue()
    stc1=Stack()
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    actual=queue.stc1.__str__()
    expected='rear->5->10->15->20->front'
    assert actual == expected

def test_Happy_Path_dequeue():
    queue = Pseudo_Queue()
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    queue.dequeue()
    expected = 'rear->5->10->15->front'
    actual= queue.stc1.__str__()
    assert actual == expected
 
def test_failure1():
    queue = Pseudo_Queue()
    queue.dequeue()
    actual = queue.dequeue().__str__()
    expected = "Empty Stack Empty Stack"
    assert actual== expected

def test_failure2():
    queue = Pseudo_Queue()
    actual = queue.dequeue().__str__()
    expected = "Empty Stack Empty Stack"
    assert actual== expected

def test_Edge_Case():
    queue = Pseudo_Queue()
    queue.enqueue("")
    assert queue.dequeue().__str__()=="Empty Stack Empty Stack"