#==================================================#
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
#======================================================#

class Stack:
    def __init__(self):
        """
        This is initial method of class Stack,
        it has one attribute, it's called top.
        """
        self.top=None

    def push(self,value):
        """
        This is push method of class Stack,
        it has two attribute, they're called new_node, temp.
        push method use to add an item to the Stack.
        :return: None
        """
        try:
            new_node=Node(value)
            temp=self.top
            self.top=new_node
            self.top.next=temp
        except Exception as error:
            print(f"There is an error in Push of  Stack, {error} ")

    def peek(self):
        """
        This is peek method of class Stack,
        :return: the last item in The Satck.
        """
        try:
            return self.top.value
        except:
            return ("Empty Stack ")

    def pop(self):
        """
        This is pop method of class Stack,
        pop method use to remove an item from The top of The Stack.
        :return:None
        """
        try:
            if self.top:  
                temp = self.top.value
                self.top= self.top.next
                return temp
            else:
                raise Exception('Empty Stack')
        except Exception as error:
            return(f"Empty Stack {error}")

    def is_empty(self):
        """
        This is is_empty method of class Stack,
        :return: Boolean, if Stack empty retrun True, else return False.
        """
        try:
            if not self.top:
                return f"is the Stack empty : {True}"
            else:
                return f"is the Stack empty : {False}"
        except Exception as error:
            print(f"There is an error in is_empty of  Stack, {error} ") 

    def __str__(self):
        """
        This is str method of class Queue.
        :return: string
        """
        try:
            output=""
            while self.top:
                output+= f"->{self.top.value}"
                self.top=self.top.next
            return f"rear{output}->front"
        except Exception as err:
            print(f'error ::: {err}')

#============================================#

class Pseudo_Queue:
    def __init__(self):
        """
        This is initial method of class Stack,
        it has one attribute, it's called top.
        """
        self.stc1=Stack()
        self.stc2=Stack()
        

    def enqueue(self,value):
        """
        This is enqueue method of class Pseudo_Queue,
        it has two attribute, they're called new_node, temp.
        push method use to add an item to the Queue.
        :return: None
        """
        try:
            if not value:
                return "invalid input"
            self.stc1.push(value)
            return self.stc1
        except Exception as error:
           print (f"There is error in enqueue of Pseudo_Queue, the error {error}")

    def dequeue(self):
        """
        This is dequeue method of class Pseudo_Queue,
        it has one attribute, it's called value.
        dequeue method use to pop an item from the front of Queue.
        :return: None
        """
        try:
            pointer = self.stc1.top
            while pointer:
                value_to_queue = self.stc1.pop()
                self.stc2.push(value_to_queue)
                pointer = pointer.next

            holder = self.stc2.pop()

            pointer2 = self.stc2.top
            while pointer2:
                value_back_to_stack = self.stc2.pop()
                self.stc1.push(value_back_to_stack)
                pointer2 = pointer2.next
            return holder
        except Exception as err:
            print (f"There is error in dequeue of Pseudo_Queue, the error {err}")

#========================================================================#

if __name__=="__main__":
    queue=Pseudo_Queue()
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    print(queue.stc1)
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    queue.enqueue(5)
    print(queue.dequeue())
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    print(queue.stc1)
    





