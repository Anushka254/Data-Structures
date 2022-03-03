class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
        
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.LinkedList.head
        self.LinkedList.head = new_node
        
    def pop(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            temp_node = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return temp_node
        
    def peek(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            temp_node = self.LinkedList.head.value
            return temp_node
        
s = Stack()
startover = True
while startover:
    print("1. PUSH AN ELEMENT INTO THE STACK")
    print("2. POP AN ELEMENT FROM THE STACK")
    print("3. FIND TOPMOST ELEMENT IN THE STACK")
    print("4. CHECK IF THE STACK IF IS EMPTY.")
    print("5. PRINT THE STACK")
    print("6. EXIT")
    ans = int(input("ENTER A CHOICE: "))
    
    if ans == 1:
        ele = int(input("ENTER THE VALUE: "))
        s.push(ele)
    elif ans == 2:
        s.pop()
    elif ans == 3:
        print(s.peek())
    elif ans == 4:
        print(s.isEmpty())
    elif ans == 5:
        print(s)
    else:
        startover = False
