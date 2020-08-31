from  data_structures_and_algorithm.stack_and_queue.stacks_and_queues import Node,Stack,Queue
import pytest


# 1- Can successfully push onto a stack
def test_push_stack():
    stack=Stack()
    stack.push(5)
    actual=stack.peek()
    expected=5
    assert  expected == actual

# 2- Can successfully push multiple values onto a stack
def test_multipush_stack():
    stack=Stack()
    stack.push(5)
    stack.push(6)
    stack.push(7)
    expected=[5,6,7]
    actual=stack.items
    assert actual == expected

# 3- Can successfully pop off the stack
def test_pop_stack():
    stack=Stack()
    stack.push(5)
    expected= "Empty Stack "
    actual = stack.pop()
    assert actual == expected

# 4- Can successfully empty a stack after multiple pops
def test_multipop_stack():
    stack=Stack()
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.pop()
    stack.pop()
    stack.pop()
    expected = None
    actual = stack.top
    assert actual == expected

# 5- Can successfully peek the next item on the stack
def test_peek_stack():
    stack=Stack()
    stack.push(5)
    assert stack.peek() == 5

# 6- Can successfully instantiate an empty stack
def test_empty_stack():
    stack=Stack()
    assert  stack.top == None

# 7- Calling pop or peek on empty stack raises exception
def test_peek_stack():
    stack=Stack()
    expected="Empty Stack "
    actual_1=stack.peek()
    actual_2=stack.pop()
    assert actual_1==actual_2 == expected

# 8- Can successfully enqueue into a queue
def test_push_queue():
    queue=Queue()
    queue.enqueue(5)
    assert queue.peek() == 5

# 9- Can successfully enqueue multiple values into a queue
def test_multipush_queue():
    queue=Queue()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    assert queue.peek() == 7

# 10- Can successfully dequeue out of a queue the expected value
def test_pop_queue():
    queue=Queue()
    actual = queue.dequeue()
    expected = "Empty Queue "
    assert actual == expected

# 11- Can successfully peek into a queue, seeing the expected value
def test_peek_queue():
    queue=Queue()
    queue.enqueue(5)
    assert queue.peek() == 5

# 12- Can successfully empty a queue after multiple dequeues
def test_peek_queue():
    queue=Queue()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty() == True

# 13- Can successfully instantiate an empty queue
def test_is_empty_queue():
    queue=Queue()
    assert queue.front == None

# 14- Calling dequeue or peek on empty queue raises exception
def test_call_is_empty_queue():
    queue=Queue()
    actual_1=queue.peek()
    actual_2=queue.dequeue()
    expected="Empty Queue "
    assert expected == actual_1 == actual_2
