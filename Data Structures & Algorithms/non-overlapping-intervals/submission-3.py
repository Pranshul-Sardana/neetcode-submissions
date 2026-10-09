class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Sort
        intervals.sort(key=lambda x:x[0])

        #Define end
        end_val = intervals[0][1]
        remove = 0

        #Iterate
        for item in intervals[1:]:
            if item[0] < end_val:
                remove += 1
                end_val = min(end_val, item[1])
            else:
                end_val = item[1]

        return remove