from data_structures_and_algorithm.tree.tree import Node,Binary_Tree

def test_pre_order():
    tree = Binary_Tree(10)
    tree.root.left = Node(9)
    tree.root.left.left = Node(7)
    tree.root.left.right = Node(8)
    tree.root.right = Node(16)
    tree.root.right.left= Node(11)
    tree.root.right.right = Node(17)
    expected = " 10 -->> 9 -->> 7 -->> 8 -->> 16 -->> 11 -->> 17 -->>"
    actual = tree.contains("pre_order")
    assert actual == expected

def test_in_order():
    tree = Binary_Tree(10)
    tree.root.left = Node(9)
    tree.root.left.left = Node(7)
    tree.root.left.right = Node(8)
    tree.root.right = Node(16)
    tree.root.right.left= Node(11)
    tree.root.right.right = Node(17)
    actual = tree.contains("in_order")
    expected = " 7 -->> 9 -->> 8 -->> 10 -->> 11 -->> 16 -->> 17 -->>"
    assert actual == expected

def test_post_order():
    tree = Binary_Tree(10)
    tree.root.left = Node(9)
    tree.root.left.left = Node(7)
    tree.root.left.right = Node(8)
    tree.root.right = Node(16)
    tree.root.right.left= Node(11)
    tree.root.right.right = Node(17)
    actual = tree.contains("post_order")
    expected = " 7 -->> 8 -->> 9 -->> 11 -->> 17 -->> 16 -->> 10 -->>"
    assert actual == expected