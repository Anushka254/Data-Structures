class node:
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # to insert values in the beginning    
    def insertbeg(self, data):
        newnode = node(data, self.head)
        self.head = newnode

    # to insert values at the end    
    def insertend(self, data):
        if self.head is None:
            self.head = node(data, None)
            return

        temp = self.head

        while temp.link:
            temp = temp.link

        temp.link = node(data, None)

    # to insert values in any index    
    def insertm(self, index, data):
        if index==0:
            self.insertbeg(data)
            return

        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                newnode = node(data, temp.link)
                temp.link = newnode
                break

            temp = temp.link
            count += 1

    # to delete a value from any specific index        
    def delete(self, index):

        if index==0:
            self.head = self.head.link
            return

        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                temp.link = temp.link.link
                break

            temp = temp.link
            count+=1
    
    # to delete a node from the beginning
    def deletebeg(self):
        if self.head is None:
            print("Linkedlist is already empty.")
            return
        else:
            self.head = self.head.link
            
    # to delete a node from the end
    def deleteend(self):
        if self.head is None:
            print("Linkedlist is already empty.")
        else:
            n = self.head
            while n.link.link is not None:
                n = n.link
            n.link = None
    
    # to print the Linked List    
    def display(self):
        if self.head is None:
            print("Underflow")
            return
        temp = self.head
        while temp:
            print(temp.data, " ", end="")
            temp = temp.link
        print()

    # returns the length of the linked list    
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count+=1
            temp = temp.link

        print(count)
    
    

# driver code
sll = SinglyLinkedList()
startover = True
while startover:
    print("1. CREATION OF THE NODE")
    print("2. INSERTION IN THE BEGINNING OF THE NODE")
    print("3. INSERTION AT THE END OF THE NODE")
    print("4. INSERTION AT ANY SPECIFIC INDEX")
    print("5. DELETION AT THE BEGINNING OF THE NODE")
    print("6. DELETION AT THE END OF THE NODE")
    print("7. DELETION AT ANY SPECIFIC INDEX")
    print("8. LENGTH OF THE LINKED LIST")
    print("9. DISPLAY THE LINKED LIST")
    print("10. EXIT")
    ans = int(input("ENTER A CHOICE: "))
    
    if ans == 2:
        ele = int(input("ENTER THE VALUE TO BE APPENDED: "))
        sll.insertbeg(ele)
    elif ans == 3:
        ele = int(input("ENTER THE VALUE TO BE APPENDED: "))
        sll.insertend(ele)
    elif ans == 4:
        ele = int(input("ENTER THE VALUE TO BE APPENDED: "))
        pos = int(input("ENTER THE INDEX VALUE OF THE NEW NODE: "))
        sll.insertm(pos,ele)
    elif ans == 5:
        sll.deletebeg()
    elif ans == 6:
        sll.deleteend()
    elif ans == 7:
        pos = pos = int(input("ENTER THE INDEX VALUE OF THE NODE TO BE DELETED: "))
        sll.delete(pos)
    elif ans == 8:
        sll.length()
    elif ans == 9:
        sll.display()
    else:
        startover = False
