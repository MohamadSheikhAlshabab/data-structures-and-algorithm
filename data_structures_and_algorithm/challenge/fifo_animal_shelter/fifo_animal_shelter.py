class Animal_Shelter:
    def __init__(self):
        """
        This is __init__ method of Animal_Shelter.
        it has two attribute, self.cats, and self.dogs,
        they're assigen to the class Queue.
        """
        self.cats=Queue()
        self.dogs=Queue()

    def enqueue(self,animal_name,animal_type):
        """
        This is enqueue method of class Animal_Shelter,
        it has two attribute, they're called animal_name, animal_type.
        push method use to add an item to the Queue.
        :return: None
        """
        try:
            if animal_type.upper() == 'CAT':
                new_animal=Cat(animal_name)
                self.cats.enqueue(new_animal)
            elif animal_type.upper()  == 'DOG':
                new_animal=Dog(animal_name)
                self.dogs.enqueue(new_animal)
            else :
                return None
        except Exception as err:
            print(f'There is error in enqueue method of class Animal_Shelter : {err}')


    def dequeue(self,animal_type):
        """
        removes the node from the front of the queue, and returns the node’s value
        """
        try:
            if animal_type.upper() == 'CAT':
                return self.cats.dequeue()
            elif animal_type.upper() == 'DOG':
                return self.dogs.dequeue()
            else :
                return None
        except Exception as err:
            print(f'There is error in dequeue method of class Animal_Shelter : {err}')

class Cat:
    def __init__(self,value):
        """
        This is __init__ method of the class Cat.
        it has one attribute, it's called value.
        """
        self.value=value
        self.type="cat"
        self.next=None

class Dog:
    def __init__(self,value):
        """
        This is __init__ method of the class Dog.
        it has one attribute, it's called value.
        """
        self.value=value
        self.type="dog"
        self.next=None


class Queue:
    """
    this class will create a queue
    """
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,new_animal):
        """
        This is enqueue method of class Queue,
        it has one attribute, it's called new_animal.
        push method use to add an item to the Queue.
        :return: None
        """
        try:
            new_node = new_animal
            if not self.front and not self.rear:
                self.front = new_node
                self.rear = new_node
            old_rear = self.rear
            self.rear = new_node
            old_rear.next = self.rear
        except Exception as err:
            print(f'There is error in enqueue method of class Queue : {err}')
        

    def dequeue(self):
        """
        removes the node from the front of the queue, and returns the node’s value
        """
        try:
            first_node = self.front
            self.front = self.front.next
            return first_node.value
        except Exception as err:
            print(f'There is error in dequeue method of class Queue : {err}')
            return "Queue is empty"

    def __str__(self):
        """
        this method creates a readable output for the user
        """
        try:
            output = ''
            current = self.front
            while current: 
                output += f"<{current.value}->"
                current = current.next
            output += f"{current}"
            return output
        except Exception as err:
            print(f'This is error in __str__: {err}')


if __name__ == "__main__":
    shelter = Animal_Shelter()
    shelter.enqueue("matrix","dog")
    shelter.enqueue("poppy","dog")
    shelter.enqueue("sherry","dog")
    shelter.enqueue("bob","dog")
    shelter.enqueue("blacky","cat")

    print(shelter.dequeue('dog'))
    print(shelter.dequeue('dog'))
    print(shelter.dequeue('cat'))
    print(shelter.dequeue('catff'))

