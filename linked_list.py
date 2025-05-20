class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linkedlist:
    def __init__(self):
        self.head = None

    #-----------------------------------------------------------------TRAVERSING A LINKED LIST------------------------------------------------------------
    def print_ll(self):
        if self.head is None:
            print("It's empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    #---------------------------------------------------------------- ADDING A NEW ELEMENT IN THE BEGINNING----------------------------------------------------
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    #------------------------------------------------------------------- ADDING A NEW ELEMENT AT THE END------------------------------------------------------
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    #------------------------------------------------------------------ ADDING A NEW ELEMENT AFTER A GIVEN NODE------------------------------------------------
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print('The given node is not available in the list')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    #------------------------------------------------------------------ ADDING A NEW ELEMENT BEFORE A GIVEN NODE------------------------------------------------
    def add_before(self, data, x):
        if self.head is None:
            print('Linked list is empty')
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print('The element is not found')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    #------------------------------------------------------------------ DELETING A NODE FROM THE BEGINNING ----------------------------------------------------------------------------
    def delete_begin(self):
        if self.head is None:
            print('The linked list is empty')
        else:
            self.head = self.head.ref

    #------------------------------------------------------------------ DELETING A NODE FROM THE END ----------------------------------------------------------------------------------
    def delete_end(self):
        if self.head is None:
            print('The linked list is empty')
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    #------------------------------------------------------------------ DELETING A NODE FROM THE SPECIFIED VALUE ---------------------------------------------------------------------------------
    def delete_by_value(self, x):
        if self.head is None:
            print('The linked list is empty')
            return
        if self.head.data == x:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print('The given node is not there in the list')
        else:
            n.ref = n.ref.ref
            
    #---------------------------------------------------------------------Find the Length of a Linked List------------------------------------------------------------------------------------    
            
    def get_length(self):
        count = 0
        n = self.head
        while n is not None:
            count += 1
            n = n.ref
        return count

    #--------------------------------------------------------------------Search for an Element in a Linked List------------------------------------------

    def search(self, x):
        pos = 0
        n = self.head
        while n is not None:
            if n.data == x:
                return pos  
            n = n.ref
            pos += 1
        return -1  


 #--------------------------------------------------------------------------Reverse a Linked List (Iterative)---------------------------------------------

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.ref
            current.ref = prev
            prev = current
            current = next_node
        self.head = prev
#--------------------------------------------------------------------------------Bubble sort------------------------------------------------------------
    
    
    def bubble_sort(self):
        if self.head is None or self.head.ref is None:
            return
        sorted = False
        while not sorted:
            sorted = True
            current = self.head
            while current.ref is not None:
                if current.data > current.ref.data:
                    current.data, current.ref.data = current.ref.data, current.data
                    sorted = False
                current = current.ref



# -------------------- MENU FOR ADDING/VIEWING DATA -------------------------

ll = Linkedlist()

while True:
    print("\n--- MENU ---")
    print("1. Add at beginning")
    print("2. Add at end")
    print("3. Add after a node")
    print("4. Add before a node")
    print("5. Delete from beginning")
    print("6. Delete from end")
    print("7. Delete by value")
    print("8. Print linked list")
    print("9. Exit")
    
    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        data = input("Enter data to add at beginning: ")
        ll.add_begin(data)
    elif choice == "2":
        data = input("Enter data to add at end: ")
        ll.add_end(data)
    elif choice == "3":
        data = input("Enter data to add: ")
        x = input("Enter the node after which to insert: ")
        ll.add_after(data, x)
    elif choice == "4":
        data = input("Enter data to add: ")
        x = input("Enter the node before which to insert: ")
        ll.add_before(data, x)
    elif choice == "5":
        ll.delete_begin()
    elif choice == "6":
        ll.delete_end()
    elif choice == "7":
        x = input("Enter the value to delete: ")
        ll.delete_by_value(x)
    elif choice == "8":
        ll.print_ll()
    elif choice == "9":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
        
        

