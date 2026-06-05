class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsMap = {num:idx for idx, num in enumerate(nums)}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in numsMap and numsMap[diff] != i:
                if numsMap[diff] < i:
                    return [numsMap[diff], i]
                else:
                    return [i, numsMap[diff]]

        return []
