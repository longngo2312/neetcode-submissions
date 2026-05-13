class Solution:
    def isValid(self, s: str) -> bool:
        #initialize stack 
        stack = []
        #using hashmap as the map for closing and opening bracket 
        closeToOpen = {")":"(", "}":"{", "]":"["}
        #loop through brackets in s 
        for bracket in s:
            #if the bracket in s is a close bracket 
            if bracket in closeToOpen:
                # check if stack is not empty and the top of stack match with the value of the hashmap 
                if stack and stack[-1] == closeToOpen[bracket]:
                    #then the brackets are opened and closed correctly we can remove the value from the stack 
                    stack.pop()
                #if stack is empty or the top of stack doesn't match then s is not a valid string 
                else: 
                    return False 
            #if bracket in s is open we can append to the stack 
            else:
                stack.append(bracket)
        #only return True if stack is empty 
        return True if not stack else False 