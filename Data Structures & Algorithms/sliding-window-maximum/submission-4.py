class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        #(nums, index)
        res = []

        l = 0
        r = 0
        
        while r < len(nums):
            while dq and dq[-1][0] < nums[r]:
                    dq.pop()
                    
            dq.append((nums[r],r))
            if (r-l+1) > k:
                l+=1
                while dq[0][1] < l:
                    dq.popleft()
            if (r-l+1) == k:
                res.append(dq[0][0])
            r+=1
        return res


                
        