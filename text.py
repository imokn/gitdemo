#Description :For suffix operation
class Stack:
    def __init__(self):   
        self.items = [] 
 
    def push(self, item):        
        self.items.append(item) 
 
    def pop(self):      
        if self.is_empty():             
            raise Exception('stackIsEmpty')         
        else:             
            return self.items.pop() 
 
    def peek(self):    
        if self.is_empty():             
            raise Exception('stackIsEmpty')         
        else:             
            return self.items[-1] 
 
    def is_empty(self):      
        return self.items == [] 
 
    def size(self):       
        return len(self.items)

Num = Stack()
Ops = input().split()
for i in range(len(Ops)):
    if Ops[i] == '+':
        b = Num.pop()
        a = Num.pop()
        Num.push(a + b)
    elif Ops[i] == '-':
        b = Num.pop()
        a = Num.pop()
        Num.push(a - b)
    elif Ops[i] == '*':
        b = Num.pop()
        a = Num.pop()
        Num.push(a * b)
    elif Ops[i] == '/':
        b = Num.pop()
        a = Num.pop()
        Num.push(a / b)
    else:
        Num.push(int(Ops[i]))