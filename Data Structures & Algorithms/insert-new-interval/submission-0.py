class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i, item in enumerate(intervals):
            if newInterval[1] < item[0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > item[1]:
                res.append(item)

            else:
                newInterval = [min(item[0], newInterval[0]), max(item[1], newInterval[1])]
                #print(newInterval)

        res.append(newInterval)

        return res