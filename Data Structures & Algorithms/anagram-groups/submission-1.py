class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strMap = {}

        for string in strs:
            setStr = sorted(string)
            newStr = ", ".join(setStr)
            if newStr in strMap:
                strMap[newStr].append(string)
            else:
                strMap[newStr] = [string]
        
        return [lst for lst in strMap.values()]
        