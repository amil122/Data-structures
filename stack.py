#####################################################################  STACK #######################################################################################
                                                                                                                                                                                                                
stack = []
def push():
    if len(stack) == n :
        print('the stack is full')
    else :
        element = int(input('enter the number you wanted to insert'))
        stack.append(element)
        print(stack)
def pop_element():
    if len(stack) == 0:
        print('it is empty stack')
    else:
        element = stack.pop
        print('the removed element is ',element)
n = int(input('enter the limit of a stack'))
while True:
    print('select the operation you want to do it 1.Push , 2.Pop, 3.quit')
    choice = int(input())
    if choice == 1 :
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3 :
        break
    else :
        print('enter the correct options')

class Stack:
    def __init__(self, n):
        self.stack = []
        self.n = n

    def push_element(self, item):
        if len(self.stack) == self.n:
            print('Stack is full')
        else:
            self.stack.append(item)
            print(self.stack)

    def pop_element(self):
        if len(self.stack) == 0:
            print('The stack is empty')
        else:
            self.stack.pop()
            print(self.stack)

    def size(self):
        print(len(self.stack))

    def top_element(self):
        if len(self.stack) == 0:
            print('The stack is empty')
        else:
            print(self.stack[-1])

# Example usage:
limit = int(input("Enter the limit for the stack: "))
stack = Stack(limit)

while True:
    print("\nMenu:")
    print("1. Push element")
    print("2. Pop element")
    print("3. Get size of stack")
    print("4. Get top element of stack")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter element to push: ")
        stack.push_element(item)
    elif choice == 2:
        stack.pop_element()
    elif choice == 3:
        stack.size()
    elif choice == 4:
        stack.top_element()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")

from queue import Queue
class StackUsingQueue:
    def __init__(self):
        self.queue = Queue()

    def push(self, item):
        self.queue.put(item)
        # Rotate the elements so that the newly added element becomes the front
        for i in range(self.queue.qsize() - 1):
            self.queue.put(self.queue.get())


    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.queue.get()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.queue.queue[0]

    def is_empty(self):
        return self.queue.empty()

    def size(self):
        return self.queue.qsize()
    def display(self):
        return self.queue.queue

# Example usage:
stack = StackUsingQueue()
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(60)
stack.push(80)
print(stack.is_empty())
print(stack.display())

print("Top of the stack:", stack.peek())  # Output: 3

print("Popped item:", stack.pop())        # Output: 3
print("Top of the stack after popping:", stack.peek())


def sort_stack(input_stack):
    temp_stack = []
    while input_stack:
        temp = input_stack.pop()
        while temp_stack and temp_stack[-1] > temp:
            input_stack.append(temp_stack.pop())
        temp_stack.append(temp)
    return temp_stack

# Example usage
stack = [34, 3, 31, 98, 92, 23]
sorted_stack = sort_stack(stack)
print("Sorted Stack:", sorted_stack)