class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        t = 0
        reached = set()
        curr = 0
        graph = defaultdict(list)
        hp = [(0, k)]
        for source, target, time in times:
            graph[source].append((time, target))
    
        
        while hp:
            w1, n1 = heapq.heappop(hp)
            if n1 in reached:
                continue
            reached.add(n1)
            t = w1
            for w2, n2 in graph[n1]:
                if n2 not in reached:
                    heapq.heappush(hp, (w1+w2, n2))
        if len(reached) == n:
            return t
        else:
            return -1


        return res