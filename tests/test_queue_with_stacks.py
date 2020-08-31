from data_structures_and_algorithm.challenge.queue_with_stacks.queue_with_stacks import Pseudo_Queue
import pytest

def test_Happy_Path_enqueue():
    queue = Pseudo_Queue()
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    actual=queue.__str__()
    expected='TOP-> {5}->{10}->{15}->{20}->NULL'
    assert actual == expected

def test_Happy_Path_dequeue():
    queue = Pseudo_Queue()
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    queue.dequeue()
    expected = "TOP-> {5}->{10}->{15}->NULL"
    actual= queue.__str__()
    assert actual == expected
 
def test_failure1():
    queue = Pseudo_Queue()
    queue.dequeue()
    actual = queue.dequeue().__str__()
    expected = "Empty Queue"
    assert actual== expected

def test_failure2():
    queue = Pseudo_Queue()
    actual = queue.dequeue().__str__()
    expected = "Empty Queue"
    assert actual== expected

def test_Edge_Case():
    queue = Pseudo_Queue()
    queue.enqueue("")
    assert queue.dequeue().__str__()=="Empty Queue"