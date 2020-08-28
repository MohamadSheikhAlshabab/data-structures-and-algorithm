from  data_structures_and_algorithm.stack_and_queue.stacks_and_queues import (Node,Stack,Queue,)

# 1- Can successfully push onto a stack
def test_push_stack():
    stack=Stack()
    assert stack.push(5) == 5

# 2- Can successfully push multiple values onto a stack
def test_multipush_stack():
    stack=Stack()
    stack.push(5)
    stack.push(6)
    stack.push(7)
    assert stack.peek() == 7

# 3- Can successfully pop off the stack
def test_pop_stack():
    stack=Stack()
    stack.push(5)
    assert stack.pop() == None

# 4- Can successfully empty a stack after multiple pops
def test_multipop_stack():
    stack=Stack()
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    assert stack.pop() == None

# 5- Can successfully peek the next item on the stack
def test_peek_stack():
    stack=Stack()
    stack.push(5)
    assert stack.peek() == 5

# 6- Can successfully instantiate an empty stack
def test_empty_stack():
    stack=Stack()
    assert  stack = None

# 7- Calling pop or peek on empty stack raises exception
def test_peek_stack():
    stack=Stack()
    assert self.assertTrue("Error" ,stack.peek())

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
    queue.enqueue(5)
    assert queue.dequeue() == 5

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
    queue.dequeue(5)
    queue.dequeue(6)
    queue.dequeue(7)
    assert queue.is_empty() == True

# 13- Can successfully instantiate an empty queue
def test_is_empty_stack():
    stack=Stack()
    assert stack.is_empty() == True

# 14- Calling dequeue or peek on empty queue raises exception
def test_is_empty_queue():
    queue=Queue()
    assert self.assertTrue("Error" ,queue.peek())
