from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def partition(l, r):
            pivotI = r
            pivotD = (points[pivotI][0]**2) + (points[pivotI][1]**2)
            i = l
            for j in range(l, r):
                currD =(points[j][0]**2) + (points[j][1]**2)
                if currD < pivotD:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[pivotI] = points[pivotI], points[i]
            return i
        
        left, right = 0, len(points) - 1
        while left<=right:
            pivot = partition(left, right)
            if pivot == k:
                break
            elif pivot < k:
                left = pivot + 1
            else:
                right = pivot - 1
        
        return points[:k]
