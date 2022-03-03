class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        if self.head is None:
            print("UNDERFLOW")
        else:
            temp = self.head
            while temp:
                print(temp.data, " ", end = " ")
                temp=temp.next
    
    def insertbeg(self,data):
        newNode = Node(data)
        temp = self.head
        #temp.prev = newNode
        newNode.next = temp
        self.head = newNode
        
    def insertend(self,data):
        newNode = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp
        
    def insertpos(self,pos,data):
        newNode = Node(data)
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next
        newNode.prev = temp
        newNode.next = temp.next
        temp.next.prev = newNode
        temp.next = newNode
        
    def deletebeg(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None
                
    def deleteend(self):
        temp = self.head.next
        before = self.head
        while temp.next is not None:
            temp = temp.next
            before = before.next
        before.next = None
        temp.prev = None
        
    def deletepos(self,pos):
        temp = self.head.next
        before = self.head
        for i in range(1,pos-1):
            temp=temp.next
            before=before.next
        before.next = temp.next
        temp.next.prev = before
        temp.next = None
        temp.prev = None
                
# driver code
dll = DoublyLinkedList()
startover = True
while startover:
    print("1. CREATION OF THE NODE")
    print("2. INSERTION IN THE BEGINNING OF THE NODE")
    print("3. INSERTION AT THE END OF THE NODE")
    print("4. INSERTION AT ANY SPECIFIC INDEX")
    print("5. DELETION AT THE BEGINNING OF THE NODE")
    print("6. DELETION AT THE END OF THE NODE")
    print("7. DELETION AT ANY SPECIFIC INDEX")
    print("8. DISPLAY THE LINKED LIST")
    print("10. EXIT")
    ans = int(input("ENTER A CHOICE: "))
    
    if ans == 1:
        ele = int(input("ENTER A VALUE: "))
        newNode = Node(ele)
        dll.head(newNode)
    if ans == 2:
        ele = int(input("ENTER THE VALUE TO BE APPENDED: "))
        dll.insertbeg(ele)
    elif ans == 3:
        ele = int(input("ENTER THE VALUE TO BE APPENDED: "))
        dll.insertend(ele)
    elif ans == 4:
        ele = int(input("ENTER THE VALUE TO BE APPENDED: "))
        pos = int(input("ENTER THE INDEX VALUE OF THE NEW NODE: "))
        dll.insertpos(pos,ele)
    elif ans == 5:
        dll.deletebeg()
    elif ans == 6:
        dll.deleteend()
    elif ans == 7:
        pos = int(input("ENTER THE INDEX VALUE OF THE NODE TO BE DELETED: "))
        dll.deletepos(pos)
    elif ans == 8:
        dll.display()
    else:
        startover = False
