class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight = 0
        l, r = 0, len(heights) - 1

        while l < r:
            if heights[l] < heights[r]:
                maxHeight = (heights[l] * (r-l)) if (heights[l] * (r-l)) > maxHeight else maxHeight
                l += 1
            else:
                maxHeight = (heights[r] * (r-l)) if (heights[r] * (r-l)) > maxHeight else maxHeight
                r -= 1

        return maxHeight