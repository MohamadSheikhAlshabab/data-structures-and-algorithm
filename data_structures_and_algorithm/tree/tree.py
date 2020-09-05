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
    
if __name__ == "__main__":
    tree = Binary_Tree(10)
    tree.root.left = Node(9)
    tree.root.left.left = Node(7)
    tree.root.left.right = Node(8)
    tree.root.right = Node(16)
    tree.root.right.left= Node(11)
    tree.root.right.right = Node(17)

    print("pre_order",tree.contains("pre_order"))
    print("in_order",tree.contains("in_order"))
    print("post_order",tree.contains("post_order"))
