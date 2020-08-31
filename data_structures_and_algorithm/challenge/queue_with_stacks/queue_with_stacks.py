class Node():
    def __init__(self,value):
        """
        this is the initial method for class Node,
        it has two attributes:
        1- the value: it contents the value of node.
        2- the next: it contents the next's node.
        """
        self.value=value
        self.next=None
    

class Pseudo_Queue:
    def __init__(self):
        """
        This is initial method of class Stack,
        it has one attribute, it's called top.
        """
        self.top_stack_1=None
        self.bottom_stack_1=None
        self.items_1=[]
        self.items_3=[]

    def enqueue(self,value):
        """
        This is enqueue method of class Pseudo_Queue,
        it has two attribute, they're called new_node, temp.
        push method use to add an item to the Queue.
        :return: None
        """
        # Push of Stack_1
        try:
            new_node=Node(value)
            if self.top_stack_1 == None:
                self.top_stack_1=new_node
                self.items_1.append(self.top_stack_1.value)
            else:
                current=self.top_stack_1
                # current_2=self.top_stack_2
                print("top",current.value)
                while current.next:
                    current=current.next
                current.next=self.bottom_stack_1
                current.next=new_node
                self.items_1.append(current.next.value)
                print(self.items_1,"items")
            self.items_3=self.items_1[:]
            self.items_3.reverse()
            print(self.items_3,"reverse")
            print( new_node.value)
            return( new_node.value,self.items_3)
        except Exception as error:
            print (f"There is error in __init__ of LinkedList, the error {error}")
        
    def dequeue(self):
        """
        This is dequeue method of class Pseudo_Queue,
        it has one attribute, it's called value.
        dequeue method use to pop an item from the front of Queue.
        :return: None
        """
        try:
            if self.top_stack_1:
                temp_2 = self.top_stack_1
                self.top_stack_1 = self.top_stack_1.next
                self.top_stack_1.next=temp_2
                self.items_1.pop()
                self.items_3.pop()
                print ("dequeue",temp_2.value)
                print ("dequeue items",self.items_1)
                print ("dequeue items",self.items_3)
                return temp_2.value
            if not self.top_stack_1:
                raise Exception('Empty Pseudo_queue')
        except Exception as error:
            return("Empty Queue")  

      
    def __str__(self):
        """
        This is toString method of LinkedList,
        to return all values as string.
        """
        try:
            items = " "
            items_2=" "
            current = self.top_stack_1
            tup=tuple( self.items_1)
            tup_2=tuple( self.items_3)
            # while current:
            #     items += f"{ {current.value} }->"
            #     current=current.next
            for i in tup:
                items += f"{ {i} }->"
            for i in tup_2:
                items_2 += f"{ {i} }->"
            items="TOP->"+items+"NULL"
            items_2="TOP->"+items_2+"NULL"
            print (f"{items}\n{items_2}")
            return items_2
        except Exception as error:
            print (f"There is error in __str__ of Pseudo_queue, the error {error}")

if __name__=="__main__":
    queue=Pseudo_Queue()
    queue.enqueue(20)
    queue.__str__()
    print("items 1",queue.items_1)
    print("items 2",queue.items_3)
    queue.enqueue(15)
    queue.__str__()
    print("items 1",queue.items_1)
    print("items 2",queue.items_3)
    queue.enqueue(10)
    queue.__str__()
    print("items 1",queue.items_1)
    print("items 2",queue.items_3)
    queue.enqueue(5)
    print("items 1",queue.items_1)
    print("items 2",queue.items_3)
    queue.__str__()
    queue.dequeue()
    queue.__str__()
    print("items 1",queue.items_1)
    print("items 2",queue.items_3)
    queue.dequeue()
    queue.__str__()
    print("items 1",queue.items_1)
    print("items 2",queue.items_3)
    queue.dequeue()
    queue.__str__()
    print("items 1",queue.items_1)
    print("items 2",queue.items_3)
    queue.dequeue()
    print("items 1",queue.items_1)
    print("items 2",queue.items_3)
    queue.__str__()