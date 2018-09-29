'''

Given two Stacks implement Queue functionality

Stack - first in last out
Queue - first in first out

'''

class Stack:
    def __init__(self):
        self.data = []
    
    def pop(self):
        if(self.data == []):
            raise ValueError
        return self.data.pop()
    
    def push(self, elt):
        self.data.append(elt)
        
    def size(self):
        return len(self.data)
    
    def peek(self):
        return self.data[len(self.data)-1]
    
class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def pop(self):
        if(self.s1.size() < 1):
            raise ValueError
        return self.s1.pop()
    
    def push(self, elt):
        while(self.s1.size() > 0):
            self.s2.push(self.s1.pop())
        self.s1.push(elt)
        while(self.s2.size() > 0):
            self.s1.push(self.s2.pop())
        
    def size(self):
        return self.s1.size()
    
    def peek(self):
        return self.s1.peek()
    
class QueueV2:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def pop(self): #O(n)
        if self.s1.size() == 0 and self.s2.size() == 0:
            raise ValueError
        if self.s2.size() == 0:
            while(self.s1.size() > 0):
                self.s2.push(self.s1.pop())
            return self.s2.pop()
        else:
            return self.s2.pop() 
    
    def push(self, elt): #O(1)
        self.s1.push(elt)
        
    def size(self):
        return self.s1.size() + self.s2.size()
    
    def peek(self):
        return self.s1.peek()
        #needs to change as well :D
    

def mainStack():
    stack = Stack()
    for x in range(6):
        stack.push(x)
    while(stack.size() > 0):
        print("Peek: " + stack.peek())
        print(stack.pop())
    
def mainQueue(queue):
    try:
        print("1", queue.pop())
        print("2", queue.pop())
        
    except ValueError:
        print("Received error - queue empty")
    
    queue.push(1)
    print("3,", queue.pop())
    
    queue.push(2)
    queue.push(3)
    
    print("4,", queue.pop()) #4, 2
    
    queue.push(4)
    queue.push(5)
    queue.push(6)
    
    count = 5
    while(queue.size() > 0):
        print(count, ", ", queue.pop())
        count += 1
    #5, 3
    #6, 4
    #...
    
    
    
    
queue = Queue()  
mainQueue(queue)
print("Switching to new queue")
print()
queuev2 = QueueV2()
mainQueue(queuev2)
    
    
