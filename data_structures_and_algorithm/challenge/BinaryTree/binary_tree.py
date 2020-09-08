from collections import defaultdict
class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
    
class Queue:
    def __init__(self):
        """
        This is initial method of class Queue,
        it has one attribute called front. 
        """
        self.elements=[]

    def enqueue(self,value):
        """
        This is enqueue method of class Queue,
        it has two attribute, they're called new_node, temp.
        push method use to add an item to the Queue.
        :return: None
        """
        try:
            self.elements.insert(0,value)
        except Exception as error:
            print(f"There is an error in enqueue of  Queue, {error} ")
        
    def dequeue(self):
        """
        This is dequeue method of class Queue,
        it has one attribute, it's called value.
        dequeue method use to pop an item from the front of Queue.
        :return: None
        """
        try:
            if not self.is_empty():
                return self.elements.pop()
        except Exception as error:
            return("Empty Queue ")
        
    def peek(self):
        """
        This is peek method of class Queue,
        :return: the last item in The Queue.
        """
        try:
            if not self.is_empty():
                return self.elements[-1].value
        except Exception as error:
            return ("Empty Queue ")
                
    def is_empty(self):
        """
        This is is_empty method of class Queue,
        :return: Boolean, if Queue empty retrun True, else return False.
        """
        try:
           return len(self.elements) ==0
        except Exception as error:
            print(f"There is an error in is_empty of  Queue, {error} ")

    def __len__(self):
        """
        This is len method of class Queue.
        :return: len of the queue
        """
        return self.size()

    def size(self):
        """
        This is size method of class Queue.
        :return: size of the queue
        """
        return len(self.elements)
  
    def __str__(self):
        """
        This is str method of class Queue.
        :return: string
        """
        output=""
        while self.front:
            output+= f"-> {self.front.value} ->"
            self.front=self.front.next
        return f"Front {output}  None"

class Binary_Tree:
    def __init__(self,root):
        self.root=Node(root)

    def pre_order(self,start,traversal):
        """
        this is the first mode of depth of tree,fill the tree starting from :
         ROOT -->> LEFT -->> RIGHT.
        """
        try:
            output=[]
            
            if start:
                traversal += str(start.value)
                traversal = self.pre_order(start.left,traversal)
                traversal = self.pre_order(start.right,traversal)
            
            x= output.append(traversal)
            c= output[0]
            return c
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

    def find_maximum_value(self,root_value):
        """
        Finds the maximum value in the binary tree.
        return: the maximum value.
        
        """
        try:
            if not self.root:
                return 'Tree is empty'
        
            else:
                max_value = root_value.value

                if root_value.left:
                    left_max = self.find_maximum_value(root_value.left)
                    if left_max > max_value:
                        max_value = left_max

                if root_value.right:
                    right_max = self.find_maximum_value(root_value.right)
                    if right_max > max_value:
                        max_value = right_max
            
            return max_value
        except Exception as error:
            print(f"There is error in find amximum value :{error}")

    def  breadth_first_traversal(self,root_value):
        """
        This is breadth_first_traversal method to travesal in the binary tree through
        breadth (level by level).
        Return: a list begin from the root, end up with the last right child in the last level.
        """
        breadth = []
        if root_value :
            queue = Queue()
            queue.enqueue(root_value)
            while len(queue)>0:
                breadth.append(queue.peek())
                temp = queue.dequeue()
                if temp.left:
                    queue.enqueue(temp.left)
                if temp.right:
                    queue.enqueue(temp.right)
        return breadth


if __name__ == "__main__":
    tree = Binary_Tree(2)
    tree.root.left = Node(7)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right = Node(5)
    tree.root.right.right= Node(9)
    tree.root.right.right.left = Node(4)
    # tree.add(15)
    # print(tree.add(15))
    print("pre_order",tree.contains("pre_order"))
    print("in_order",tree.contains("in_order"))
    print("post_order",tree.contains("post_order"))

    print(tree.find_maximum_value(tree.root))
    print(tree.breadth_first_traversal(tree.root))
 