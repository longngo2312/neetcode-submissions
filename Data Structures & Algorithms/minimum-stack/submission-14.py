class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.iteration = 1

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        elif val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        self.iteration += 1
        popValue = self.stack[-1]
        self.stack.pop()
        if popValue == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
