class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0,0,0]

        for x,y,z in triplets:
            if x== target[0] or y == target[1] or z == target[2]:
                if x > target[0] or y > target[1] or z > target[2]:
                    continue
                else:
                    res = [max(x,res[0]), max(y,res[1]), max(z,res[2])]
        
        return res == target
