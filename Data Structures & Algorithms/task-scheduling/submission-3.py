class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for t in tasks:
            count[t]+=1
        
        hp = [(-c, t) for t, c in count.items()]
        heapq.heapify(hp)

        cooldown = deque()
        time = 0
        while hp or cooldown:
            if not hp and cooldown:
                time  = cooldown[0][2]
            c, t = heapq.heappop(hp)
            if c+1 != 0:
                cooldown.append((c+1,t, time+n+1))
            time+=1
            if not hp and cooldown:
                time  = cooldown[0][2]
            while cooldown and cooldown[0][2]<=time:
                c,t,time = cooldown.popleft()
                heapq.heappush(hp, (c,t))
            if not hp and cooldown:
                time  = cooldown[0][2]
        return time
        
