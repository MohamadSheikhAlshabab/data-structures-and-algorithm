class Node:
    def __init__(self,value):
        """
        This is initial method of class Node,
        it has two attributes, they called value, next.
        """
        self.value=value
        self.next=None
    

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
            if not self.top:
                self.top=Node(value)
            else:
                new_node=Node(value)
                temp=self.top
                self.top=new_node
                new_node=temp
        except Exception as error:
            print(f"There is an error in Push of  Stack, {error} ")

    def peek(self):
        """
        This is peek method of class Stack,
        :return: the last item in The Satck.
        """
        try:
            return f"the last item in The Satck : {self.top.value}"
        except Exception as error:
            print(f"There is an error in peek of  Stack, {error} ")

    def pop(self):
        """
        This is pop method of class Stack,
        pop method use to remove an item from The top of The Stack.
        :return:None
        """
        try:
            if not self.top:
                return None
            else:
                temp=self.top
                self.top=self.top.next
                self.top.next=None
            return ("ddd",temp.value)

        except Exception as error:
            print(f"There is an error in pop of  Stack, {error} ")

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
        output=""
        while self.top:
            output+= f"-> {self.top.value} ->"
            self.top=self.top.next
        return f"Top {output}  None"

class Queue:
    def __init__(self):
        """
        This is initial method of class Queue,
        it has one attribute called front. 
        """
        self.front=None

    def enqueue(self,value):
        """
        This is enqueue method of class Queue,
        it has two attribute, they're called new_node, temp.
        push method use to add an item to the Queue.
        :return: None
        """
        try:
            new_node=Node(value)
            temp=self.front
            self.front=new_node
            new_node=temp
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
            temp=self.front
            self.front=self.front.next
            self.front.next=temp
        except Exception as error:
            print(f"There is an error in dequeue of  Queue, {error} ")
        
    def peek(self):
        """
        This is peek method of class Queue,
        :return: the last item in The Queue.
        """
        try:
            return f"the last item in The Queue :{self.front.value}"
        except Exception as error:
            print(f"There is an error in peek of  Queue, {error} ")
                
    def is_empty(self):
        """
        This is is_empty method of class Queue,
        :return: Boolean, if Queue empty retrun True, else return False.
        """
        try:
            if not self.front:
                return f"is the Queue empty : {True}"
            else:
                return f"is the Queue empty : {False}"
        except Exception as error:
            print(f"There is an error in is_empty of  Queue, {error} ")
  
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


if __name__ == "__main__":
    stack=Stack()
    print("is_empty : ",stack.is_empty())
    # print(stack.pop())
    stack.push(5)
    print("peek : ",stack.peek())
    print("str : ",stack.__str__())
    # stack.pop()
    stack.push("50")
    print("peek : ",stack.peek())
    print("str : ",stack.__str__())
    stack.push(15)
    print("peek : ",stack.peek())
    print("str : ",stack.__str__())
    stack.push("ss")
    print("peek : ",stack.peek())
    print("str : ",stack.__str__())
    print("is_empty : ",stack.is_empty())
    # print("peek : ",stack.peek())
    # stack.pop()
    print("is_empty : ",stack.is_empty())
    # print("peek : ",stack.peek())
    print("is_empty : ",stack.is_empty())
    # print("peek : ",stack.peek())
    # stack.pop()
    print("is_empty : ",stack.is_empty())
    # print("peek : ",stack.peek())
    # stack.pop()
    # print("peek : ",stack.peek())
    print("is_empty : ",stack.is_empty())

    print("*"*50)
    queue=Queue()
    queue.enqueue("4")
    print("peek : ",queue.peek())
    queue.enqueue("40")
    print("peek : ",queue.peek())
    queue.enqueue("14")
    print("peek : ",queue.peek())
    print("str : ",queue.__str__())
    queue.enqueue("oo")
    print("dequeue : ",queue.dequeue())
    queue.dequeue()
    # print("peek : ",queue.peek())
    print("is_empty : ",queue.is_empty())