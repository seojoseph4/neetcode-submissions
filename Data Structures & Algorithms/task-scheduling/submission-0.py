class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for letter in tasks:
            count[letter] = count.get(letter,0) + 1
        # print(count)
        mh = []
        for c in count:
            mh.append([-count[c],c])
        heapq.heapify(mh)
        sch = deque()
        res = 0
        while mh or sch:
            res+=1
            if sch and sch[0][0] == res:
                ready, count, val = sch.popleft()
                heapq.heappush(mh, [count, val])
            if mh:
                count, val = heapq.heappop(mh)
                count = count +1
                if count != 0:
                    sch.append([res+n+1, count, val])
        return res

            



