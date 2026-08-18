class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i,subset):
            res.append(subset.copy())
            for j in range(i, len(nums)):
                if j >i and nums[j] == nums[j-1]:
                    continue
            # include
                subset.append(nums[j])
                dfs(j+1,subset)
                subset.pop()
            
            return
        
        dfs(0, [])
        return res
            



            
                
