class Node:
      def __init__(self, value = None):
            self.value = value
            self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def createCSLL(self, value):
        new_node = Node(value)
        new_node.next = None
        self.head = new_node
        self.tail = new_node
        print("Node created.")
    
    def __iter__(self):
            node = self.head
            while node:
                yield node
                node = node.next
                if node == self.tail.next:
                    break
    def insert_beg(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head
    def insert_mid(self,mid_node, value):
        if mid_node is None:
            print("Mentioned node doesn't exist")
            return
        new_node = Node(value)
        new_node.next = mid_node.next
        mid_node.next = new_node 
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
        self.tail = new_node
        self.tail.next = self.head
    
    def printlist(self):
        node_print = self.head
        while node_print:
            print(node_print.value, " ->", end=" ")
            node_print = node_print.next
            if node_print == self.tail.next:
                break
                print("\n")
    def delete_beg(self):
        if(self.head == None):
            return
        elif (self.head.next == self.tail.next):
            self.head = self.tail = None
            return
        else:
            temp_node = self.head
            self.head = self.head.next
            temp_node = None
            self.tail.next = self.head
            return
        
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
            return
    def delete_val(self, del_value):
        temp_head = self.head
        if (temp_head is not None):
            if (temp_head.value == del_value):
                self.head = temp_head.next
                temp_head = None
                return

        while (temp_head is not None):
            if temp_head.value == del_value:
                break
            prev = temp_head
            temp_head = temp_head.next

        if (temp_head == None):
            return

        prev.next = temp_head.next
        temp_head = None
        
csll = CircularSinglyLinkedList()
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
    print("9. EXIT")
    ans = int(input("ENTER A CHOICE: "))
    
    if ans == 1:
        ele = int(input("ENTER THE VALUE: "))
        csll.createCSLL(ele)
    elif ans == 2:
        ele = int(input("ENTER THE VALUE TO BE APPENDED: "))
        csll.insert_beg(ele)
    elif ans == 3:
        ele = int(input("ENTER THE VALUE TO BE APPENDED: "))
        csll.insert_end(ele)
    elif ans == 4:
        ele = int(input("ENTER THE VALUE TO BE APPENDED: "))
        pos = int(input("ENTER THE VALUE AFTER WHICH NODE TO BE APPENDED: "))
        csll.insert_mid(pos,ele)
    elif ans == 5:
        csll.delete_beg()
    elif ans == 6:
        csll.delete_end()
    elif ans == 7:
        ele = int(input("ENTER THE VALUE TO BE DELETED: "))
        csll.delete_val(ele)
    elif ans == 8:
        csll.printlist()
    else:
        startover = False
