class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
    
class Binary_Tree:
    def __init__(self,root):
        self.root=Node(root)

    def pre_order(self,start,traversal):
        """
        this is the first mode of depth of tree,fill the tree starting from :
         ROOT -->> LEFT -->> RIGHT.
        """
        try:
            if start:
                traversal += (f" {str(start.value)} -->>")
                traversal = self.pre_order(start.left,traversal)
                traversal = self.pre_order(start.right,traversal)
            # print ("pre_order : ")
            return traversal
        except Exception as error:
            print(f"Thsre is error in pre_order:{error}")

    def in_order(self,start,traversal):
        """
        this is the second mode of depth of tree,fill the tree starting from :
         LEFT-->> ROOT -->> RIGHT.
        """
        try:
            if start:
                traversal = self.in_order(start.left,traversal)
                traversal += (f" {str(start.value)} -->>")
                traversal = self.in_order(start.right,traversal)
            # print ("in_order : ")
            return traversal
        except Exception as error:
            print(f"Thsre is error in in_order:{error}")

    def post_order(self,start,traversal):
        """
        this is the third mode of depth of tree,fill the tree starting from :
          LEFT -->> RIGHT -->> ROOT.
        """
        try:
            if start:
                traversal = self.post_order(start.left,traversal)
                traversal = self.post_order(start.right,traversal)
                traversal += (f" {str(start.value)} -->>")
            # print ("post_order : ")
            return traversal
        except Exception as error:
            print(f"Thsre is error in post_order:{error}")

    def add(self,value):
        try:
            if not self.root:
                self.root=Node(value)
            else:
                new_node=Node(value)
                if new_node>=self.root:
                    self.root.right=new_node
                    return self.root.right
                elif new_node<self.root:
                    self.root.left=new_node
                    return self.root.left
        except Exception as error:
            print(f"Thsre is error in add:{error}")

    def contains (self,type_depth):
        try:
            if type_depth == "pre_order":
                return self.pre_order(self.root,"")
            elif type_depth == "in_order":
                return self.in_order(self.root,"")
            elif type_depth == "post_order":
                return self.post_order(self.root,"")
            else:
                print("Wrong type depth")
                return False 
        except Exception as error:
            print(f"There is error in contains :{error}")

def tree_intersection(tree_a, tree_b):
    """
    Find the intersection of values in two trees.
    """

    union = set({})
    intersection = set({})
    root_a = tree_a.root
    root_b = tree_b.root

    if not root_a or not root_b:
        return intersection

    walk(root_a, union, intersection)
    walk(root_b, union, intersection)

    return intersection


def walk(root, union, intersection):
    """
    In-order walk a tree adding to sets union and intersection.
    """
    if root.value in union:
        intersection.add(root.value)
    else:
        union.add(root.value)

    if root.left:
        walk(root.left, union, intersection)

    if root.right:
        walk(root.right, union, intersection)


if __name__ == "__main__":
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

    print("*"*20)
    print("pre_order",tree1.contains("pre_order"))
    print("*"*20)
    print("pre_order",tree.contains("pre_order"))
    print("*"*20)
    print("in_order",tree1.contains("in_order"))
    print("*"*20)
    print("in_order",tree.contains("in_order"))
    print("*"*20)
    print("post_order",tree1.contains("post_order"))
    print("*"*20)
    print("post_order",tree.contains("post_order"))

    print("*"*20)
    print("*"*20)
    print("*"*20)
    print(tree_intersection(tree1,tree))