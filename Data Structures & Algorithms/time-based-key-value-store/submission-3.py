class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping:
            return ""
        res = ""
        lis = self.mapping[key]
        l = 0
        r = len(lis)-1
        while l<=r :
            m = (l+r) //2
            if lis[m][0] > timestamp:
                r = m-1
            else:
                res = lis[m][1]
                l = m+1
        return res