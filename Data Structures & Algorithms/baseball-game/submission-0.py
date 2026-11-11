class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] 
        for operation in operations: 
            if operation == "+":
                score1, score2 = stack[-1], stack[-2]
                total = score1 + score2
                stack.append(total)

            elif operation == "D":
                prevScore = stack[-1]
                stack.append(prevScore * 2)
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))
            print("operation: ", operation, " stack: ", stack)
        
        return sum(stack)

