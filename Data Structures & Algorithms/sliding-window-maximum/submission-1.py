class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l = 0
        r = 0
        #keep deque decreasing
        while r < len(nums):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            if (r-l+1) > k:
                if q[0] == nums[l]:
                    q.popleft()
                l+=1
            
            if (r-l+1) == k:
                res.append(q[0])
            r+=1
        
        return res
                
            

