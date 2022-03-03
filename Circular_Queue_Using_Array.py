class CQueue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.front = -1
        self.rear = -1
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.rear + 1 == self.front:
            return True
        elif self.front == 0 and self.rear + 1 == self.maxSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.front == -1:
            return True
        else:
            return False
        
    def enqueue(self, value):
        if self.isFull():
            return "The circular queue is full"
        else:
            if self.rear + 1 == self.maxSize:
                self.rear = 0
            else:
                self.rear += 1
                if self.front == -1:
                    self.front = 0
            self.items[self.rear] = value
            return "The element is successfully inserted at the end of the Circular Queue"
        
    def dequeue(self):
        if self.isEmpty():
            return "The circular queue is empty."
        else:
            firstElement = self.items[self.front]
            front = self.front
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            elif self.front + 1 == self.maxSize:
                self.front = 0
            else:
                self.front += 1
            self.items[front] = None
            return firstElement
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[self.front]
        
size = int(input("ENTER THE SIZE OF THE CIRCULAR QUEUE: "))    
cq = CQueue(size)
startover = True
while startover:
    print("1. PUSH AN ELEMENT INTO THE QUEUE")
    print("2. POP AN ELEMENT FROM THE QUEUE")
    print("3. FIND TOPMOST ELEMENT OF THE QUEUE")
    print("4. CHECK IF THE QUEUE IF IS EMPTY.")
    print("5. CHECK IF THE QUEUE IF IS FULL.")
    print("6. PRINT THE QUEUE")
    print("7. EXIT")
    ans = int(input("ENTER A CHOICE: "))
    
    if ans == 1:
        ele = int(input("ENTER THE VALUE: "))
        cq.enqueue(ele)
        print("\n\n")
    elif ans == 2:
        cq.dequeue()
        print("\n\n")
    elif ans == 3:
        print(cq.peek())
        print("\n\n")
    elif ans == 4:
        print(cq.isEmpty())
        print("\n\n")
    elif ans == 5:
        print(cq.isFull())
        print("\n\n")
    elif ans == 6:
        print(cq)
        print("\n\n")
    else:
        startover = False 
