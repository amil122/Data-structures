class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Doublyll:
    def __init__(self):
        self.head = None

    # Forward Traversal
    def print_doublell_forward(self):
        if self.head is None:
            print('List is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data, end=' ')
                n = n.nref
            print()

    # Backward Traversal
    def print_doublell_backward(self):
        if self.head is None:
            print('List is empty')
            return
        n = self.head
        while n.nref is not None:
            n = n.nref
        while n is not None:
            print(n.data, end=' ')
            n = n.pref
        print()

    # Add to empty list
    def add_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('List is not empty')

    # Add at the beginning
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    # Add at the end
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            new_node.pref = n
            n.nref = new_node

    # Add after a node
    def add_after(self, data, x):
        if self.head is None:
            print('List is empty')
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print('Given node not found')
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    # Add before a node
    def add_before(self, data, x):
        if self.head is None:
            print('List is empty')
            return
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print('Given node not found')
        else:
            new_node = Node(data)
            new_node.nref = n
            new_node.pref = n.pref
            if n.pref is not None:
                n.pref.nref = new_node
            else:
                self.head = new_node
            n.pref = new_node

    # Delete from beginning
    def delete_begin(self):
        if self.head is None:
            print('List is empty')
            return
        if self.head.nref is None:
            self.head = None
        else:
            self.head = self.head.nref
            self.head.pref = None

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print('List is empty')
            return
        if self.head.nref is None:
            self.head = None
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    # Delete by value
    def delete_by_value(self, x):
        if self.head is None:
            print('List is empty')
            return
        if self.head.data == x:
            if self.head.nref is None:
                self.head = None
            else:
                self.head = self.head.nref
                self.head.pref = None
            return
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print("Value not found")
        elif n.nref is None:
            n.pref.nref = None
        else:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
    
    #Find the Middle Element of a Doubly Linked List
    def find_middle(self):
        if self.head is None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast and fast.nref:
            slow = slow.nref
            fast = fast.nref.nref

        print("Middle element is:", slow.data)

    #Remove Duplicates from a Sorted Doubly Linked List
    def remove_duplicates(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current.nref is not None:
            if current.data == current.nref.data:
                next_node = current.nref.nref
                current.nref = next_node
                if next_node:
                    next_node.pref = current
            else:
                current = current.nref




dll = Doublyll()
dll.add_empty(10)
dll.add_end(20)
dll.add_begin(5)
dll.add_after(15, 10)
dll.add_before(8, 10)

print("Forward Traversal:")
dll.print_doublell_forward()

print("Backward Traversal:")
dll.print_doublell_backward()

dll.delete_begin()
dll.delete_end()
dll.delete_by_value(10)

print("After Deletions (Forward):")
dll.print_doublell_forward()


dll.print_doublell_forward()  # Before removing duplicates
dll.remove_duplicates()
dll.print_doublell_forward()  # After removing duplicates

dll.find_middle()
