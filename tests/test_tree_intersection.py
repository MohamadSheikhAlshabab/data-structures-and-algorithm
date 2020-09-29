from data_structures_and_algorithm.tree_intersection.tree_intersection import Node, Binary_Tree, tree_intersection, walk
import pytest

def test_tree_intersection():
    """
    The intersection of two trees is found.
    """

    tree1 = Binary_Tree(150)
    tree1.root.left = Node(100)
    tree1.root.left.left = Node(75)
    tree1.root.left.right = Node(160)
    tree1.root.left.right.left = Node(125)
    tree1.root.left.right.right = Node(175)
    tree1.root.right = Node(250)
    tree1.root.right.left= Node(200)
    tree1.root.right.right = Node(350)
    tree1.root.right.right.left = Node(300)
    tree1.root.right.right.right = Node(500)

    tree = Binary_Tree(42)
    tree.root.left = Node(100)
    tree.root.left.left = Node(15)
    tree.root.left.right = Node(160)
    tree.root.left.right.left = Node(125)
    tree.root.left.right.right = Node(175)
    tree.root.right = Node(600)
    tree.root.right.left= Node(200)
    tree.root.right.right = Node(350)
    tree.root.right.right.left = Node(4)
    tree.root.right.right.right = Node(500)

    expected = {160, 100, 200, 175, 500, 125, 350}
    actual = tree_intersection(tree, tree1)
    
    assert actual == expected