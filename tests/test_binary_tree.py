from data_structures_and_algorithm.challenge.BinaryTree.binary_tree import Queue,Binary_Tree,Node

def test_breadth_search():
    tree = Binary_Tree(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    actual = tree.breadth_first_traversal(tree.root)
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    assert actual == expected

def test_breadth_search_2():
    tree = Binary_Tree(5)
    tree.root.left = Node(55)
    tree.root.right = Node(19)
    actual = tree.breadth_first_traversal(tree.root)
    expected = [5,55,19]
    assert actual == expected

def test_breadth_search_3():
    tree = Binary_Tree(-11)
    tree.root.left = Node(55)
    tree.root.right = Node(-19)
    actual = tree.breadth_first_traversal(tree.root)
    expected = [-11,55,-19]
    assert actual == expected

def test_empty_tree():
    tree = Binary_Tree("")
    assert tree.breadth_first_traversal(tree.root) == [""]