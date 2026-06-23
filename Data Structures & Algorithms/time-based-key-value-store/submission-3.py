class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append([timestamp, value])
        print(self.hm)

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hm[key]
        res = ""

        l, r = 0, len(arr) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            print(f"before: {arr[l: r + 1]}, midval: {arr[m]} ")

            if timestamp >= arr[m][0]:
                res = arr[m][1]
                l = m + 1
            else:
                r = m - 1
            
            print(f"after: {arr[l: r + 1]}, midval: {arr[m]} ")
        
        return res
                #ex: hmVals['a'] -> vals = [x, y, z], arr = [[2 (ts), 1 (idx)]], hmVals['a'][[arr[0][1]]] = y
            