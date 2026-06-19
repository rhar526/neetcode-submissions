class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False
        
        outer = matrix
        low, high = 0, len(outer) - 1

        while low <= high:
            
            if len(outer) == 1:
                l, h = 0, len(outer[0]) - 1

                while l <= h:
                    m = l + ((h - l) // 2)

                    if outer[0][m] > target:
                        h = m - 1
                    elif outer[0][m] < target:
                        l = m + 1
                    else:
                        return True
                
                return False
            elif len(outer) == 2:
                if outer[0][0] <= target and target <= outer[0][-1]:
                    outer = [outer[0]]
                else:
                    outer = [outer[1]]
            else:
                
                mid = low + ((high - low) // 2)

                if outer[mid + 1][0] > target:
                    outer = outer[0:mid + 1]
                    high = len(outer) - 1
                elif outer[mid - 1][-1] < target:
                    outer = outer[mid:high + 1]
                    low = 0
            
                
                
                