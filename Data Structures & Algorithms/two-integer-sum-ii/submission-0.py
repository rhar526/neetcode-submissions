class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #go backwards

        i, j = (len(numbers) - 1), 0

        while j < i:
            diff = target - numbers[i]

            if diff < numbers[j]:
                i -=1
                j = 0
                continue
            elif numbers[j] == diff:
                return [j + 1, i + 1]
            else:
                j += 1
                

            
                