class Solution:
    def isValid(self, s: str) -> bool:
        
        closedMap = {')':'(', ']':'[', '}':'{'}
        openStack = []

        for c in s:
            if c not in closedMap:
                openStack.append(c)
            elif len(openStack) == 0: #every closed has a corresponding open: if x is closed, stack must have open in it
                return False
            elif openStack.pop() != closedMap[c]:
                return False
        
        if len(openStack) != 0:
            return False

        return True
