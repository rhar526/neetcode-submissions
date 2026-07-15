class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = {}, {}
        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1

        matches = 0
        for c in s1Count:
            if s1Count[c] == s2Count.get(c, 0):
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == len(s1Count):
                return True

            rChar = s2[r]
            s2Count[rChar] = s2Count.get(rChar, 0) + 1
            if rChar in s1Count:
                if s1Count[rChar] == s2Count[rChar]:
                    matches += 1
                elif s1Count[rChar] + 1 == s2Count[rChar]:
                    matches -= 1

            lChar = s2[l]
            s2Count[lChar] -= 1
            if lChar in s1Count:
                if s1Count[lChar] == s2Count[lChar]:
                    matches += 1
                elif s1Count[lChar] - 1 == s2Count[lChar]:
                    matches -= 1
            l += 1

        return matches == len(s1Count)