class Twitter:

    def __init__(self):
        self.follows = {}
        self.tweets = {}
        self.count = 0 
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1
        if userId not in self.tweets:
            mh = [[self.count,tweetId]]
            self.tweets[userId] = mh
        else:
            self.tweets[userId].append([self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        biglist = []
        if userId in self.tweets:
            for count, tweet in self.tweets[userId]:
                heapq.heappush(biglist, [-count, tweet])
        if userId in self.follows:
            for id in self.follows[userId]:
                for count, tweet in self.tweets[id]:
                    heapq.heappush(biglist, [-count, tweet])
        res = []
        curr = 0
        while biglist and len(res) < 10:
            _, tweetId = heapq.heappop(biglist)
            res.append(tweetId)
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.follows:
            temp = set()
            temp.add(followeeId)
            self.follows[followerId] = temp
        else:
            self.follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)
        
