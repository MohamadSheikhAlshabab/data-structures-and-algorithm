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
                while current.next != None:
                    current=current.next
                current.next=new_node

        except Exception as error:
            print (f"There is error in __init__ of LinkedList, the error {error}")

    def includes(self,text,key):
        """
        This is includes method of LinkedList,
        to return boolean text if value exist in
        LinkedList or not.
        """
        try:
            if not text:
                return False
            if text.value==key:
                return True
            return self.includes(text.next,key)
        except Exception as error:
            print (f"There is error in __init__ of LinkedList, the error {error}")

    def toString(self):
        """
        This is toString method of LinkedList,
        to return all values as string.
        """
        try:
            current=self.head
            output=[]
            while not current:
                current=current.next
                output.append(current.value)
            print (output)
        except Exception as error:
            print (f"There is error in __init__ of LinkedList, the error {error}")


if __name__=="__main__":
    list1= LinkedList()
    list1.insert(12)
    list1.insert(5)
    list1.insert(7)
    list1.insert(99)
    print(list1)
    print(list1.includes("12",12),"1111")
    print(list1.includes("99",99),"222222")
    list1.toString()
    print(list1)