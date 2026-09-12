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
        res= []
        if userId in self.tweets:
            index = len(self.tweets[userId]) - 1
            time, tweetId = self.tweets[userId][index]
            heapq.heappush(hp, (-time, tweetId,userId, index))
        
        if userId in self.followers:     
            for user in self.followers[userId]:
                if user not in self.tweets:
                    continue
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]
                heapq.heappush(hp, (-time, tweetId,user, index))

        while len(res) < 10 and hp:
            time, id, user, index = heapq.heappop(hp)
            res.append(id)
            if index-1 >=0:
                time, tweetId = self.tweets[user][index-1]
                heapq.heappush(hp, (-time, tweetId,user, index-1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)
        
