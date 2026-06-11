class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack: list(list(int)) = [] # i.e.[[1, 2], [3,4]] idx0 = start, idx1 = height
        maxArea: int = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                start, height = stack.pop()
                area = (i - start) * height
                maxArea = area if area > maxArea else maxArea
        
            stack.append([start, h])
        
        if stack:
            for bar in stack:
                area = (len(heights) - bar[0]) * bar[1]
                maxArea = area if area > maxArea else maxArea

        return maxArea