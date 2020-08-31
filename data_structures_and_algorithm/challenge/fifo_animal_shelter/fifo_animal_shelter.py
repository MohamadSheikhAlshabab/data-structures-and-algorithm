class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Animal_Shelter:
    def __init__(self):
        self.front = None
        self.rear = None
        self.next = None

    def __str__(self):
        """
        This is toString method of LinkedList,
        to return all values as string.
        """
        current = self.front
        output = ''
        while current:
            output += f"{current.value}->"
            current = current.next
        return output

    def enqueue(self, value):
        """
        This is enqueue method of class Animal_Shelter,
        it has two attribute, they're called new_node, temp.
        push method use to add an item to the Queue.
        :return: None
        """
        
        new_node = Node(value)
        if not self.front and not self.rear:
            self.front = new_node
            self.rear = new_node

        old_rear = self.rear
        self.rear = new_node
        old_rear.next = self.rear

    def dequeue(self,pref):
        """
        This is dequeue method of class Animal_Shelter,
        it has one attribute, it's called value.
        dequeue method use to pop an item from the front of Queue.
        :return: None
        """
        pass

class Cat:
    def __init__(self):
        pass

class Dog:
    def __init__(self):
        pass

if __name__ == "__main__":
    matrix = Dog()
    poppy = Dog()
    sherry = Cat()
    bob = Dog()
    blacky = Cat()
    henry = Dog()
    shelter = Animal_Shelter()
    shelter.enqueue(matrix)
    shelter.enqueue(poppy)
    shelter.enqueue(sherry)
    shelter.enqueue(bob)
    shelter.dequeue('Dog')
    shelter.enqueue(blacky)
    # print(shelter.dequeue('cat'))
    shelter.enqueue(henry)
    # print(shelter.dequeue('Dog'))
    # print(shelter.dequeue('cat'))
    print(shelter.__str__())