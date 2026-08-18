class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        seeni = False
        seenj = False
        seenk = False
        for x in range(len(triplets)):
            i,j,k = triplets[x]
            if i > target[0] or j > target[1] or k > target[2]:
                continue
            if i == target[0]:
                seeni = True
            if j == target[1]:
                seenj = True
            if k == target[2]:
                seenk = True
        
    
        return seeni and seenj and seenk


        