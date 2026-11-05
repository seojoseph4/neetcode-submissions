class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()

        res = []

        l = 0
        for r in range(len(nums)):
            curr = nums[r]
            while dq and dq[-1][0] < curr:
                dq.pop()
            dq.append([curr,r])
            if (r-l+1) > k:
                l+=1
                if dq and dq[0][1] < l:
                    dq.popleft()
            if (r-l+1) == k:
                res.append(dq[0][0])
        
        return res
