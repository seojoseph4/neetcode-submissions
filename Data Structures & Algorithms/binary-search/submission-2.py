class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, len(nums)-1)
    def helper(self, nums: List[int], target: int, l: int, r: int) ->int:
        if l >r:
            return -1
        mid = (l+r+1)//2
        print(l)
        print(r)
        print(mid)
        if nums[mid] == target:
            return mid
        if nums[mid] <target:
            return self.helper(nums, target, mid+1, r)
        else:
            return self.helper(nums, target, l, mid-1)
        