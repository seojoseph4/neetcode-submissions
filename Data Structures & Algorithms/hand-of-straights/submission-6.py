class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counter = defaultdict(int)
        for i in hand:
            counter[i]+=1

        for key in sorted(counter):
            n = counter[key]
            for i in range(key+1,key+groupSize):
                if n <= counter[i]:
                    counter[i]-=n
                else:
                    return False
        
        return True
