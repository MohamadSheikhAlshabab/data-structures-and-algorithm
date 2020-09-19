from data_structures_and_algorithm.challenge.BinaryTree.binary_tree import Binary_Tree,Node
import pytest

def test_1():
    tree = Binary_Tree(2)
    tree.root.left = Node(7)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right = Node(5)
    tree.root.right.right= Node(9)
    tree.root.right.right.left = Node(4)
    actual = tree.find_maximum_value(tree.root)
    expected = 11
    assert actual == expected

def test_2():
    tree = Binary_Tree(-1)
    tree.root.left = Node(-13)
    tree.root.right = Node(-5)
    tree.root.left.left = Node(-2)
    tree.root.left.right = Node(-6)
    tree.root.left.right.left = Node(-5)
    tree.root.left.right.right = Node(-11)
    tree.root.right = Node(-5)
    tree.root.right.right= Node(-9)
    tree.root.right.right.left = Node(-4)
    actual = tree.find_maximum_value(tree.root)
    expected = -1
    assert actual == expected

def test_3():
    tree = Binary_Tree("")
    actual = tree.find_maximum_value(tree.root)
    expected = ""
    assert actual == expected