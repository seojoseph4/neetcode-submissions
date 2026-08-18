class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        count ={}
        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n] = 1

        buckets = []
        for i in range (len(nums)):
            buckets.append([])

        for freq in count:
            buckets[count[freq]-1].append(freq)
        
        for i in range(len(buckets)-1,-1,-1):
            for j in buckets[i]:
                if k >0:
                    res.append(j)
                    k-=1
        return res
                



        