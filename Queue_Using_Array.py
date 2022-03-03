class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return "Queue is empty"
        else:
            return "Queue is not empty"
        
    def enqueue(self, value):
        self.items.append(value)
        return "The element is successfully inserted at the end of Queue."
    
    def dequeue(self):
        if self.isEmpty():
            return "The Queue does not exist."
        else:
            return ("The topmost element is", self.items.pop(0))

    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.items[0]
        
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
