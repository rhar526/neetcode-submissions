class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedStrs = []
        for s in strs:
            encodedStrs.append(str(len(s)))
            encodedStrs.append("#")
            encodedStrs.append(s)
            #lengthOfStr + # + Str = lengthOfStr#Str
        return "".join(encodedStrs)

    def decode(self, s: str) -> List[str]:
        lstOfStrs = []
        i = 0

        while i < len(s):
            j = i #i always points to the start of a block of format lengthOfStr#Str
            while s[j] != '#': 
                #because lengthOfStr is of type str, start from i and end at j
                #j will store the index of last digit of the number, as the next char is always #
                j += 1 #increment until '#'

            lengthOfStr = int(s[i:j]) 
            #str from i to j, i.e. in "23#", i points to '2', and j points to '#'
            #s[i:j] is a str including index i, excluding index j, so '23' is converted to int
            i = j + 1 #j + 1 is index of Str
            j = i + lengthOfStr 
            lstOfStrs.append(s[i:j]) 
            i = j #sets i to the start of next block

        return lstOfStrs