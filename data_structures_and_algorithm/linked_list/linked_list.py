class Node():
    def __init__(self,value):
        """
        this is the initial method for class Node,
        it has two attributes:
        1- the value: it contents the value of node.
        2- the next: it contents the next's node.
        """
        try:
            self.value=value
            self.next=None

        except Exception as error:
            print (f"There is error in __init__ of Node, the error {error}")

class LinkedList():

    def __init__(self):

        """
        This is the initial method of LinkedList,
        it has only one attribute, which is head.
        the head is a reference to the first node always.
        """
        try:
            self.head=None

        except Exception as error:
            print (f"There is error in __init__ of LinkedList, the error {error}")

    def insert(self,value):

        """
        This is inserting method of LinkedList,
        functionality of this method to insert a new
        node on LinkedList.
        """
        try:
            new_node=Node(value)
            if self.head == None:
                self.head=new_node
            else:
                current=self.head
                while current.next:
                    current=current.next
                current.next=new_node
            print( new_node.value)
            return( new_node.value)
        except Exception as error:
            print (f"There is error in __init__ of LinkedList, the error {error}")

    def includes(self,value):
        """
        This is includes method of LinkedList,
        to return boolean text if value exist in
        LinkedList or not.
        """
        try:

            current_node = self.head
            while current_node.next != None:
                if current_node.value == value:
                    return True
                else:
                    current_node = current_node.next
            return False

        except Exception as error:
            print (f"There is error in __init__ of LinkedList, the error {error}")

    def to_string(self):
        """
        This is to_string method of LinkedList,
        to return all values as string.
        """
        try:

            current=self.head
            output=[]
            while current:
                output.append(current.value)
                current=current.next
            return output

        except Exception as error:
            print (f"There is error in __init__ of LinkedList, the error {error}")
    
    def items(self):
        sum=1
        current=self.head
        if current:
            while current.next:
                sum+=1
                current=current.next
            return sum
        else:
            return None

    def append_value(self, value):
        """
        This is append method of LinkedList,
        to add a values at the end of the LinkedList.
        """
        new_node = Node(value)
        if not self.head :
            self.head = new_node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self,next_node,value):
        """
        This is insert_before method of LinkedList,
        to add a value before the specific node.
        """
        try:

            if next_node == None:
                print("Doesn't exist")
            new_node=Node(value)
            current=self.head
            if next_node==current:
                new_node=Node(value)
                new_node.next=self.head
                self.head=new_node
                return
            while current:
                if current.next==next_node:
                    next_node.next=current.next
                    current.next=new_node
                    return

                else:
                    current = self.head
                while current.next != None:
                    if current.next.value == next_node:
                        temp = current.next
                        current.next = new_node
                        new_node.next = temp
                        return 
                    else:
                        current = current.next
                return "doesn't exist"
        except Exception as error:

            print (f"There is an error in append of LinkList {error}")
        

    def insert_after(self,pre_node,value):
        """
        This is insert_after method of LinkedList,
        to add a value after the specific node.
        """
        try:

            if pre_node==None:
                print("doesn't exist")
                return
            new_node=Node(value)
            new_node.next=pre_node.next
            pre_node.next=new_node


        except Exception as error:
            print (f"There is an error in insert_after of LinkList {error}")

    def reverse(self):

        """
        This method to reverse all nodes,
        make the last node is first one and 
        vice versa.
        """
        try:
            prev=None
            next=None
            curr= self.head
            while curr == None:
                next=curr.next
                prev = curr
                curr=next
                curr.next=prev
            self.head=prev
        except Exception as error:
            print (f"There is an error in append of LinkList {error}")
        
            

    def kth_from_end(self,k):
        """
        This method to search in linked list if have it value
        equal to k integer, then return value of index's node 
        that have it, reference point is the last node in linked list.
        """
        try:
            found=None
            curr=self.head
            while curr==k:
                found=curr
                curr=curr.next
            return curr
        except Exception as error:
            print (f"There is an error in append of LinkList {error}")

if __name__=="__main__":
    list1= LinkedList()
    list1.insert(12)
    # print(list1.to_string,"qqqq")
    list1.insert(5)
    # print(list1,"qqqqq")
    list1.insert(7)

    # print(list1)
    list1.insert(99)
    # print(list1)
    list1.to_string()
    print(list1)
    list1.insert_before(list1.head.next,'15')
    print(list1.to_string())
    list1.insert_after(list1.head.next.next,6)
    print(list1.includes(5))
    print(list1.includes(66))
    print(list1.to_string())
    print(list1.reverse())
    print(list1.to_string())
    print(list1.kth_from_end(5))
    print(list1.to_string())
    

