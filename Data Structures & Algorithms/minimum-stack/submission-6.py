class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] 

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            if self.minStack[-1] >= val:
                self.minStack.append(val)
                print("minStack",self.minStack)
            self.stack.append(val)
            print("curr stack: ", self.stack)
        

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.minStack[-1]:
            self.minStack.pop()
        print(" minStack", self.minStack)
        print(" stack", self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
