class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        counter = 0

        for i, firstNum in enumerate(nums):
            counter += 1
            newList = nums[i + 1: length]
            for j, secondNum in enumerate(newList):
                if (firstNum + secondNum) == target:
                    return [i, j + counter]

        