class Solution:
    def isPalindrome(self, s: str) -> bool:

        chars = [c.lower() for c in s if c.isalnum()]
        fwdptr = 0
        revptr = (len(chars) - 1)
        print(chars)

        while fwdptr < revptr:
            if chars[fwdptr] != chars[revptr]:
                return False

            fwdptr +=1
            revptr -=1
        
        return True