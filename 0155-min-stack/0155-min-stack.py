class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, value: int) -> None:
        if  len(self.minstack)==0 :
            self.minstack.append(value)
        
        else:
            if self.minstack[-1]>value:
                self.minstack.append(value)

            else:
                self.minstack.append(self.minstack[-1])

        self.stack.append(value)
        

    def pop(self) -> None:
        if len(self.stack )==0:
            return None
        
        self.minstack.pop()

        return self.stack.pop()
        

    def top(self) -> int:
        if not self.stack:
            return -1
        
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()