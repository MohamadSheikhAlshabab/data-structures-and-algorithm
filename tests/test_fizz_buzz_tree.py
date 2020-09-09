from data_structures_and_algorithm.challenge.fizz_buzz_tree.fizz_buzz_tree import Queue,Binary_Tree,Node,FizzBuzzTree

import pytest

@pytest.fixture
def data():
    tree = Binary_Tree(2)
    tree.root.left = Node(7)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right = Node(5)
    tree.root.right.right= Node(9)
    tree.root.right.right.left = Node(4)

    empty= Binary_Tree("")
    return {'t':tree,'e':empty}




def test_fizz_buzz_fizzbuzz_add_correctly(data):
    actual = FizzBuzzTree(data['t'])
    expected = ['2', '7', '2', 'Fizz', 'Buzz', '1', '1', 'Buzz', 'Fizz', '4']
    assert  actual == expected

def test_if_tree_is_empty(data):
    actual = FizzBuzzTree(data['e'])
    expected = "The tree is an empty"
    assert  actual == expected
  


