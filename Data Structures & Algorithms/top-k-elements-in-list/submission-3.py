class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = {}

        for num in nums:
            if num in freqMap:
                freqMap[num]+= 1
            else:
                freqMap[num] = 1

        topKFreqs = (sorted([freq for freq in freqMap.values()]))[-k:]

        keys = [k for k,v in freqMap.items() if v in topKFreqs]
        return keys

      

