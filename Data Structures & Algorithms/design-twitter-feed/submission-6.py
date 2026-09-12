class Twitter:

    def __init__(self):
        self.followers = {}
        self.tweets = {}
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = deque()
        self.tweets[userId].append((self.time, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()
        self.time+=1


    def getNewsFeed(self, userId: int) -> List[int]:
        hp = []
        if userId in self.tweets:
            for t in self.tweets[userId]:
                heapq.heappush(hp, t)
                if len(hp) > 10:
                    heapq.heappop(hp)


        if userId in self.followers:     
            for user in self.followers[userId]:
                if user not in self.tweets:
                    continue
                for t in self.tweets[user]:
                    heapq.heappush(hp,t)
                    if len(hp) > 10:
                        heapq.heappop(hp)
        # print(hp)
        res = []
        while hp:
            time, id = heapq.heappop(hp)
            res.append(id)
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)
        
