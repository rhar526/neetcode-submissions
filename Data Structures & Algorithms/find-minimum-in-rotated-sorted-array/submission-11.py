class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        while l < r:

            mid = l + ((r-l)//2)
            
            if nums[l] == nums[mid] and nums[l] > nums[r]:
                return nums[r]
            elif nums[l] > nums[mid] and nums[r] > nums[mid]:
                r = mid
            elif nums[l] < nums[mid] and nums[r] < nums[mid]:
                l = mid
            else:
                return nums[l]


                