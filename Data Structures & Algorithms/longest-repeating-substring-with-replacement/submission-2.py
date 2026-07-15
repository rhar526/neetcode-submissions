class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = {}
        l, res, maxFrq = 0, 0, 0
        lst = list(s)

        for r in range(len(lst)):
            charFreq[lst[r]] = charFreq.get(lst[r], 0) + 1
            maxFrq = max(maxFrq, charFreq[lst[r]])
           
            if (r - l + 1) - maxFrq > k:
                charFreq[lst[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res