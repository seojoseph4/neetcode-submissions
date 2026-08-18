class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

      intervals.sort(key = lambda i: i[0])
      currEnd= intervals[0][1]
      currStart = intervals[0][0]
      res = []
      for i in range(1,len(intervals)):
        if currEnd < intervals[i][0]:
            res.append([currStart, currEnd])
            currStart = intervals[i][0]
            currEnd = intervals[i][1]
        else:
            currEnd = max(currEnd, intervals[i][1])

      res.append([currStart, currEnd])
      return res

        