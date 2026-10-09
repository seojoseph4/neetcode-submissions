class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize !=0:
            return False
        
        hm = defaultdict(int)


        for i in range(len(hand)):
            hm[hand[i]]+=1

        for x in sorted(hm):
            c = hm[x]
            if c == 0:
                continue
            for card in range(x, x+groupSize):
                if hm[card] < c:
                    return False
                hm[card]-=c
        return True