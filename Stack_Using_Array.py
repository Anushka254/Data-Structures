class Stack: 
    items = [];

    def __init__(self):
        self.items = []

    def  push(self, element): 
        self.items.append(element) 

    def  pop(self): 
        if len(self.items) == 0:
            print('Can not pop form an empty list')
        self.items.pop();
        print('Last item has been poped from the list')

    def  printStack(self): 
        for i in self.items:
            print(i)

    def isEmpty(self):
        print(len(self.items) == 0)

    def peek(self):
        if len(self.items) == 0:
            print('Stack is Empty')
        print(self.items[len(self.items) - 1]) ;
         
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
        s.peek()
    elif ans == 4:
        s.isEmpty()
    elif ans == 5:
        s.printStack()
    else:
        startover = False
