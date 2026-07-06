class Solution:
    def isValid(self, s: str) -> bool:
        closeMap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []
        for bracket in s:
            if bracket in closeMap:
                if stack and stack[-1] == closeMap[bracket]:
                    stack.pop()
                    continue
                else:
                    return False 
            stack.append(bracket)
        return len(stack) == 0