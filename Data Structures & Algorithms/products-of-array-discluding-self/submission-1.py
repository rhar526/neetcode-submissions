class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        revNums = nums[::-1]
        prefix = []
        suffix = []
        res = []
        i = 0
        
        while i < len(nums):
            if len(prefix) == 0 and len(suffix) == 0:
                prefix.append(nums[i]) 
                suffix.append(revNums[i])
                i += 1
                continue

            prefix.append(prefix[i - 1] * nums[i])
            suffix.insert(0, suffix[0] * revNums[i])
            i += 1
        
        j = 0
        while j < len(nums):
            pre, suf = 0, 0
            if j - 1 < 0:
                pre = 1
            else:
                pre = prefix[j - 1]
            
            if j + 1 >= len(suffix):
                suf = 1
            else: 
                suf = suffix[j + 1]
                
            res.append(pre*suf)
            j += 1
        
        return res
        
        
