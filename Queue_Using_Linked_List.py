class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return "Queue is empty"
        else:
            return "Queue is not empty"
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.LinkedList.head == None:
            self.LinkedList.head = new_node
            self.LinkedList.tail = new_node
        else:
            self.LinkedList.tail.next = new_node
            self.LinkedList.tail = new_node
            
    def dequeue(self):
        if self.isEmpty():
            return "The Queue does not exist."
        else:
            temp_node = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
            return temp_node
    def peek(self):
        if self.isEmpty():
            return "The Queue does not exist."
        else:
            return ("The topmost element is", self.LinkedList.head)
        
q = Queue()
startover = True
while startover:
    print("1. PUSH AN ELEMENT INTO THE QUEUE")
    print("2. POP AN ELEMENT FROM THE QUEUE")
    print("3. FIND TOPMOST ELEMENT OF THE QUEUE")
    print("4. CHECK IF THE QUEUE IF IS EMPTY.")
    print("5. PRINT THE QUEUE")
    print("6. EXIT")
    ans = int(input("ENTER A CHOICE: "))
    
    if ans == 1:
        ele = int(input("ENTER THE VALUE: "))
        q.enqueue(ele)
    elif ans == 2:
        q.dequeue()
    elif ans == 3:
        print(q.peek())
    elif ans == 4:
        print(q.isEmpty())
    elif ans == 5:
        print(q)
    else:
        startover = False    
