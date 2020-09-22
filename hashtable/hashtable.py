class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

class HashMap:
    def __init__(self):
        self.size=1024
        self.map = self.size * [None]

    def add(self,key,value):
        key_hash = self.hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
                else:
                    self.map[key_hash].append(list([key_value]))
                    return True

    def get(self,key):
        key_hash = self.hash(key) 
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]: 
                if pair[0] == key:
                    return pair[1]

    # def contains(self,key):
    #     hashed_key = self.hash(key)
    #     print(hashed_key,key,"1111")
    #     hm = HashMap()
    #     # g=hm.get(key)
    #     # k=self.hash(g)
    #     print(hm(key),"222")
       
    #     # if  hm.keys():
    #     #     return True

    #     # else:
    #     #     return False

    def set(self,key,value):
        hashed_key = self.hash(key)
        if self.map[hashed_key] == None:
            self.map[hashed_key] = LinkedList()
        self.map[hashed_key].add((key, value))

    def hash(self, key):
        hashed_total = 0
        for char in key:
            hashed_total += ord(char)
        return hashed_total*19 % self.size

    
if __name__ == "__main__":
    hm = HashMap()
    hm.add("1", "sachin")
    hm.add("2", "sehwag")
    hm.add("3", "ganguly")
    hm.add("4", "srinath")
    hm.add("5", "kumble")
    hm.add("6", "dhoni")
    hm.add("7", "kohli")
    hm.add("8", "pandya")
    hm.add("9", "rohit")
    hm.add("10", "dhawan")
    hm.add("11", "shastri")
    hm.add("12", "manjarekar")
    hm.add("13", "gupta")
    hm.add("14", "agarkar")
    hm.add("15", "nehra")
    hm.add("16", "gawaskar")
    hm.add("17", "vengsarkar")
    print("*"*50)
    print(hm.hash("1"))
    print(hm.hash("2"))
    print(hm.hash("3"))
    print(hm.hash("4"))
    print(hm.hash("5"))
    print(hm.hash("6"))
    print(hm.hash("7"))
    print(hm.hash("8"))
    print(hm.hash("9"))
    print(hm.hash("10"))
    print(hm.hash("11"))
    print(hm.hash("12"))
    print(hm.hash("13"))
    print(hm.hash("14"))
    print(hm.hash("15"))
    print(hm.hash("16"))
    print(hm.hash("17"))
    print("*"*50)
    print("*"*50)
    print(hm.get("1"))
    print(hm.get("2"))
    print(hm.get("3"))
    print(hm.get("4"))
    print(hm.get("5"))
    print(hm.get("6"))
    print(hm.get("7"))
    print(hm.get("8"))
    print(hm.get("9"))
    print(hm.get("10"))
    print(hm.get("11"))
    print(hm.get("12"))
    print(hm.get("13"))
    print(hm.get("14"))
    print(hm.get("15"))
    print(hm.get("16"))
    print(hm.get("17"))
    print("*"*50)
    # print(hm.contains("1"))
    # print(hm.contains("2"))
    # print(hm.contains("3"))
    # print(hm.contains("4"))
    # print(hm.contains("5"))
    # print(hm.contains("6"))
    # print(hm.contains("7"))
    # print(hm.contains("8"))
    # print(hm.contains("9"))
    # print(hm.contains("10"))
    # print(hm.contains("11"))
    # print(hm.contains("12"))
    # print(hm.contains("13"))
    # print(hm.contains("14"))
    # print(hm.contains("15"))
    # print(hm.contains("16"))
    # print(hm.contains("17"))
    # print(hm.contains("18"))