class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx in reversed(range(len(nums))):
            i, j = 0, idx - 1
            if nums[idx] + nums[i] + nums[j] == 0 and sorted([nums[i], nums[j], nums[idx]]) not in res:
                    res.append(sorted([nums[i], nums[j], nums[idx]]))

            while i != j and idx >= 2:
                if nums[idx] + nums[i] + nums[j] > 0:
                    if j - 1 == i:
                        break
                    j -= 1
                else:
                    if i + 1 == j:
                        break
                    i += 1
                if nums[idx] + nums[i] + nums[j] == 0 and sorted([nums[i], nums[j], nums[idx]]) not in res:
                    res.append(sorted([nums[i], nums[j], nums[idx]]))
    
                    
        return res

                



