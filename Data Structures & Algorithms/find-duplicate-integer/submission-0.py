class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #O(n) memory solution:

        vals = set()

        for num in nums:
            if num in vals:
                return num
            else:
                vals.add(num)