from typing import List
from collections import defaultdict
from collections import deque
import heapq
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictfee = defaultdict(set)
        self.dicttweet = defaultdict(deque)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """

        self.dicttweet[userId].append((self.timer,tweetId))
        self.timer+=1
        if len(self.dicttweet[userId])>10:
            self.dicttweet[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        feed = list(self.dicttweet[userId])
        heapq.heapify(feed)
        for followee in self.dictfee[userId]:
            for time,tweet in self.dicttweet[followee]:
                if len(feed)< 10:
                    heapq.heappush(feed,(time,tweet))
                elif time > feed[0][0]:
                    heapq.heappushpop(feed,(time,tweet))
        ans = []
        while len(feed)>0:
            ans.append(heapq.heappop(feed)[1])
        return ans[::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.dictfee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.dictfee[followerId]:        
            self.dictfee[followerId].remove(followeeId) 


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
T= Twitter()
T.postTweet(1,5)
print(T.getNewsFeed(1))
T.follow(1,2)
T.postTweet(2,6)
print(T.getNewsFeed(1))
T.unfollow(1,2)
print(T.getNewsFeed(1))