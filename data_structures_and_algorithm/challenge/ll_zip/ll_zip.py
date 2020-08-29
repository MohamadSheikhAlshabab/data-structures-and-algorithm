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

    def append(self,value):
        """
        This is append method of LinkedList,
        to add all values for LinkeList.
        """
        try:
            new_node=Node(value)
            if self.head==None:
                self.head=new_node
            else:
                current=self.head
                while current.next != None:
                    current=current.next
                current.next=new_node

        except Exception as error:
            print (f"There is an error in append of LinkList {error}")  
    
    def print(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

    def zip_list(self,alist):
        greater=self.head
        less=alist.head
        merge= None
        if greater and less:
            merge = greater
            greater = merge.next
        new_head=merge
        while greater and less:
            merge.next = less
            merge = less
            less = merge.next
            merge.next = greater
            merge = greater
            greater = merge.next
        if  greater == None:
            merge.next = less

if __name__=="__main__":
    list1= LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)
    print("list1 = ",list1.print())
    list2= LinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(4)
    print("list2 = ",list2.print())
    list1.zip_list(list2)
    print("list2 = ",list1.print())
    list3= LinkedList()
    list3.append(1)
    list3.append(3)
    print("list3 = ",list3.print())
    list2= LinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(4)
    print("list2 = ",list2.print())
    list3.zip_list(list2)
    print("list3 = ",list3.print())
    list1= LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)
    print("list1 = ",list1.print())
    list4= LinkedList()
    list4.append(5)
    list4.append(9)
    print("list4 = ",list4.print())
    list1.zip_list(list4)
    print("list1 = ",list1.print())