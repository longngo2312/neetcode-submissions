class MinStack:

    def __init__(self):
        self.stack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minVal = self.stack[0]
        for value in self.stack:
            print(value)
            if minVal > value:
                minVal = value
            print("new min val", minVal)
        return minVal  
            
