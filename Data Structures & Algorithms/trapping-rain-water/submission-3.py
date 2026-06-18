class Solution:
    def trap(self, height: List[int]) -> int:
        
        total = 0
        maxL, maxR = height[0], height[- 1]
        l, r = 0, len(height) - 1

        while l < r:
            
            if maxL < maxR or maxL == maxR:
                l += 1
                total += (maxL - height[l]) if maxL - height[l] > 0 else 0
                maxL = height[l] if height[l] > maxL else maxL
            else:
                r -= 1
                total += (maxR - height[r]) if maxR - height[r] > 0 else 0
                maxR = height[r] if height[r] > maxR else maxR
        
        return total
            

