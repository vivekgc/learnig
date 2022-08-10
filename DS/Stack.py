import re


class Stack:
    def __init__(self):
        self.stack = []
    
    def add(self,dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def remove(self):
        if len(self.stack) <=0:
            return ("no element in the stack")
        else:
            return self.stack.pop()

    def peek(self):     
	    return self.stack[-1]

Astack = Stack()
Astack.add("mon")
Astack.add("tue")
Astack.add("wed")
Astack.add("thur")
Astack.add("fri")
Astack.peek()
print(Astack.remove())
print(Astack.remove())
print(Astack.peek())