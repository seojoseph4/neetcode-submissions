class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hm = defaultdict(int)
        for card in hand:
            hm[card]+=1
        

        for i in sorted(hm):
            count = hm[i]
            for j in range(i+1,i+groupSize):
                if hm[j] >= count:
                    hm[j]-=count
                else:
                    return False

        
        return True