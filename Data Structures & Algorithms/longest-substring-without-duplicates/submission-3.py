class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        strArr = list(s)
        l = 0
        r = 1
        lngst = 1
        cMap = {strArr[l] : l}
        
        while r < len(strArr):
            if strArr[r] in cMap:
                l = max(l, cMap.pop(strArr[r]) + 1)
                print(f"l : {l}")
            
            cMap[strArr[r]] = r
            lngst = max(r - l + 1, lngst)
            r += 1
            print(f"r: {r}, cMap: {cMap}")
        
        return lngst