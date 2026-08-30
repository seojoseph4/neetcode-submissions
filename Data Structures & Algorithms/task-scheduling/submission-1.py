class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = defaultdict(int)
        for t in tasks:
            hm[t]+=1
        # key: name
        # value : count
        schedule = [(-v, k) for k,v in hm.items()]
        heapq.heapify(schedule)

        #[timefornext, name, count]
        delay = deque()

        res = 0
        while schedule or delay:
            # print(res)
            # print(schedule)
            # print(delay)
            # print("-")
            if schedule:
                currcount, currname = heapq.heappop(schedule)
                if currcount+1 != 0:
                    nextelement = (res+n, currname,currcount+1)
                    delay.append(nextelement)
            while delay and delay[0][0] <= res:
                top = delay.popleft()
                heapq.heappush(schedule, (top[2], top[1]))
            res+=1



        return res