class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        #find the numbers that are the closest
        r = 0
        while r < len(arr):
            if arr[r] >= x:
                break
            r+=1

        l = r-1
        while (r-l-1) < k:
            if l < 0:
                r+=1
                continue
            elif r >= len(arr):
                l-=1
                continue
            
            ldiff = abs(arr[l]-x)
            rdiff = abs(arr[r]-x)
            if ldiff < rdiff:
                l-=1
            elif rdiff < ldiff:
                r+=1
            else:
                if arr[l] < arr[r]:
                    l-=1
                else:
                    r+=1
        print(l,r)
        return arr[l+1:r]


