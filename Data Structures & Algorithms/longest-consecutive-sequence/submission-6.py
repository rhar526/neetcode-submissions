class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNumsSet = list(sorted(set(nums)))
        print(sortedNumsSet)

        if len(nums) == 0:
            return 0
        count = 1
        maxCount = 1

        for i in range(1, len(sortedNumsSet)):
            if sortedNumsSet[i] - 1 == sortedNumsSet[i-1] or sortedNumsSet[i] + 1 == sortedNumsSet[i-1]:
                count+=1
                if count > maxCount:
                    maxCount = count
            else: 
                count = 1
                if count > maxCount:
                    maxCount = count
            
        return maxCount