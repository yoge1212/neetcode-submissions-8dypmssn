class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweets = defaultdict(list)
        self.counter = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        self.tweets[userId].append((-self.counter, tweetId))

        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = list(self.tweets[userId])      
        for user in self.followMap[userId]:
            heap = heap + list(self.tweets[user])
        heapq.heapify(heap)
        top10 = []
        heapCount = len(heap)
        for i in range(10):
            if i >= heapCount:
                break
            top10.append(heapq.heappop(heap)[1])

        return top10




        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].discard(followeeId)
        
