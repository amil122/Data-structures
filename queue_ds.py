

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ QUEUE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class Queue:
    def __init__(self,n) :
        self.queue = []
        self.n = n
    def enqueue (self,item):
        if len(self.queue)== self.n:
            print('it is a empty queue')
        else :
            self.queue.append(item)
            print(self.queue)
    def dequeue(self):
        if len(self.queue)== 0 :
            print('it is empty so you cant pop the element')
        else :
            self.queue.pop(0)
            print(self.queue)
    def isEmpty(self):
        if len(self.queue) == 0:
            print('it is epmty')
        else:
            print('it is not empty')
    def front(self):
        print(self.queue[0])
    def rear(self):
        print(self.queue[-1])
queue1 = Queue(44)
queue1.enqueue(43)
queue1.enqueue(55)
queue1.enqueue(100)
queue1.dequeue()
        
class QueueUsingStack :
    def __init__(self,n) :
        self.stack1 = []
        self.stack2 = []
        self.n = n
    def enqueue(self,item):
        if len(self.stack1) == self.n :
            print('the queue is full')
        else:
            self.stack1.append(item)
        return self.stack1
    def dequeue(self):
        if not self.stack2 :
            if not self.stack1:
                return ' queue is empty'
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return (self.stack2.pop())
    def peek(self):
        if not self.stack2:
            if not self.stack1:
                return 'queue is empty'
            while self.stack1:
                 self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    
    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)


q1= QueueUsingStack(3)
print(q1.enqueue(53))
print(q1.enqueue(64))
print(q1.enqueue(34))


print(q1.dequeue())


from queue import PriorityQueue

class Queue:
    def __init__(self):
        self.queue = PriorityQueue()

    def enqueue(self, item):
        # We assign a default priority of 0 to each item
        self.queue.put(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.get()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        # Temporarily dequeue and enqueue the item to get it
        item = self.queue.get()
        self.queue.put(item)  
        return item

    def is_empty(self):
        return self.queue.empty()

    def size(self):
        return self.queue.qsize()

# Example usage:
q = Queue()
q.enqueue((1, 'apple'))
q.enqueue((2, 'banana'))
q.enqueue((3, 'orange'))

print("Size of queue:", q.size())    # Output: 3
print("Front of the queue:", q.peek())  # Output: (1, 'apple')

print("Dequeued item:", q.dequeue())  # Output: (1, 'apple')
print("Front of the queue after dequeue:", q.peek())  # Output: (2, 'banana')
