class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        close_ = {')':'(',']':'[','}':'{'}
        stack = []
        iteration = 1
        for bracket in s:
            if bracket in close_:
                if len(stack) != 0 and stack[-1] == close_[bracket]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(bracket)
        return len(stack) == 0

    