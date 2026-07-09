class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #O(1) solution:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(f"slow: {slow}, fast: {fast}")
            if slow == fast:
                break
            
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow2 == slow:
                return slow
