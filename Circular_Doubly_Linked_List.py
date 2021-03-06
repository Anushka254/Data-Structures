class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def createCDLL(self, value):
        new_node = Node(value)
        new_node.next = None
        new_node.prev = None
        self.head = new_node
        self.tail = new_node
        print("NODE CREATED")
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    def insert_beg(self, value):
        new_node =  Node(value)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head
        self.head.prev = self.tail
        
    def insert_pos(self,prev_node, value):
        if prev_node is None:
            print("Mentioned node doesn't exist")
            return

        next_node = prev_node.next 
        new_node = Node(value)
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node
        
    def insert_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        last_node = self.head
        while(last_node.next != self.head):
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
        self.tail = new_node
        self.tail.next = self.head
        self.head.prev = self.tail
        
    def print_for(self):
        if self.head == None:
            print("The linked list does not exist.")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                if temp_node == self.tail:
                    break
                temp_node = temp_node.next
                
    def print_rev(self):
        if self.head == None:
            print("The linked list does not exist.")
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                if temp_node == self.head:
                    break
                temp_node = temp_node.prev
                
    def delete_beg(self):
        if(self.head == None):
            return
        elif (self.head.next == self.tail.next):
            self.head = self.tail = None
            return
        elif (self.head is not None):
            next_node = self.head.next
            next_node.prev = None
            self.head = next_node
            self.tail.next = self.head
            self.head.prev = self.tail
            return
        
    def delete_pos(self, del_value):
        if(self.head == None):
            return
        temp_node = self.head
        found = False
        while (temp_node) :
            if(temp_node.value == del_value):
                found = True
                break
            temp_node = temp_node.next
        if (found == True):
            prev_node = temp_node.prev
            next_node = temp_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            return
        else:
            print("Element not found.")
            
    def delete_end(self):
        if(self.head == None):
            return
        elif (self.head.next == self.tail.next):
            self.head = self.tail = None
            return
        else:
            temp_node = self.head
            while (temp_node.next is not self.tail):
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
            self.tail.next = self.head
            self.head.prev = self.tail
            return

cdll = CircularDoublyLinkedList()
startover = True
while startover:
    print("1. CREATION OF THE NODE")
    print("2. INSERTION IN THE BEGINNING OF THE NODE")
    print("3. INSERTION AT THE END OF THE NODE")
    print("4. INSERTION AT THE MIDDLE")
    print("5. DELETION AT THE BEGINNING OF THE NODE")
    print("6. DELETION AT THE END OF THE NODE")
    print("7. DELETION OF A SPECIFIC NODE")
    print("8. DISPLAY THE LINKED LIST")
    print("9. DISPLAY THE LINKED LIST IN REVERSE ORDER")
    print("10. EXIT")
    ans = int(input("ENTER A CHOICE: "))
    
    if ans == 1:
        ele = int(input("ENTER THE VALUE: "))
        cdll.createCDLL(ele)
    elif ans == 2:
        ele = int(input("ENTER THE VALUE TO BE APPENDED: "))
        cdll.insert_beg(ele)
    elif ans == 3:
        ele = int(input("ENTER THE VALUE TO BE APPENDED: "))
        cdll.insert_end(ele)
    elif ans == 4:
        ele = int(input("ENTER THE VALUE TO BE APPENDED: "))
        cdll.insert_pos(prev,ele)
    elif ans == 5:
        cdll.delete_beg()
    elif ans == 6:
        cdll.delete_end()
    elif ans == 7:
        ele = int(input("ENTER THE VALUE TO BE DELETED: "))
        cdll.delete_pos(ele)
    elif ans == 8:
        cdll.print_for()
    elif ans == 9:
        cdll.print_rev()
    else:
        startover = False
