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
            current = self.head
            while current.next != None:
                if current.value == value:
                    return True
                else:
                    current = current.next
                    return False
        except Exception as error:
            print (f"There is error in __init__ of LinkedList, the error {error}")

    def to_string(self):
        """
        This is toString method of LinkedList,
        to return all values as string.
        """
        try:
            items = " "
            current = self.head
            while current:
                items += f"{ {current.value} }->"
                current=current.next
            items+="NULL"
            print (items)
            return items
            #     items.append(current.value)
            #     current = current.next
            # print(''.join(f"{ {k[1]} }->" for k in enumerate(items))+'NULL')
            # return(''.join(f"{ {k[1]} }->" for k in enumerate(items))+'NULL')
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

if __name__=="__main__":
    list1= LinkedList()
    list1.insert(12)
    list1.insert(5)
    list1.insert(7)
    list1.insert(990)
    # print(list1.to_string())
    print(list1.includes(12))
    print(list1.includes(99))
    list1.to_string()
    # print(list1)