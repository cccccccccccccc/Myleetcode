from typing import List
class Leaderboard:

    def __init__(self):
        self.playdict = {}
        self.scorelist = [0]*101

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.playdict:
            oldscore = self.playdict[playerId]
            self.scorelist[oldscore]-=1
            newscore = oldscore+score if oldscore+score <100 else 100
            self.playdict[playerId] = newscore
            self.scorelist[newscore]+=1
        else:
            self.playdict[playerId] = score
            self.scorelist[score]+=1 
    def top(self, K: int) -> int:
        sum = 0
        for i in range(101)[::-1]:
            if K <=0:
                break
            if self.scorelist[i] != 0:
                sum += min(self.scorelist[i],K)*i
                K-=self.scorelist[i]
            i-=1
        return sum
    def reset(self, playerId: int) -> None:
        oldscore = self.playdict[playerId]
        self.addScore(playerId,-oldscore)



#Your Leaderboard object will be instantiated and called as such:
obj = Leaderboard()
obj.addScore(1,80)
param_2 = obj.top(1)
print(param_2)
obj.reset(1)
print(obj.top(1))
