class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        i = 0
        j =0
        hs= set()
        while j < len(nums):
            if abs(i - j) > k:
                hs.remove(nums[i])
                i+=1
            
            if nums[j] in hs:
                return True
            
            hs.add(nums[j])
            j+=1
        return False

