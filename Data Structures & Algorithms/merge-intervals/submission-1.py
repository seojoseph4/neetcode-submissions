class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

      intervals.sort(key = lambda i :i[0])

      res = []
      currStart = intervals[0][0]
      currEnd = intervals[0][1]

      for start, end in intervals[1:]:
        if start <= currEnd:
          currEnd = max(currEnd, end)
          currStart = min(currStart, start)
        else:
          res.append([currStart, currEnd])
          currStart = start
          currEnd = end
      res.append([currStart, currEnd])
      return res