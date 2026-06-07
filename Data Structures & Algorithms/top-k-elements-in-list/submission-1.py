class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
            print(freqMap)
        
        kFreqs = sorted([vals for vals in freqMap.values()])[-k:]

        return [k for k, v in freqMap.items() if v in kFreqs]

        