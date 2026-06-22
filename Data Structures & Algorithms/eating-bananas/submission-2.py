from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l<r:
            mid = l + ((r - l)//2)

            timeArr = [ceil(pile/mid) for pile in piles]
            summedTime = sum(timeArr)

            if summedTime > h:
                l = mid + 1
            else:
                r = mid
           

            """print(timeArr)
            print(summedTime)
            print(K)
            print(r)
            print(mid)
            print(l)"""
        
        return l
