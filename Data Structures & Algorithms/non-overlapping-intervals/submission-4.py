class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Sort
        intervals.sort(key = lambda x:x[0])

        #Items to remove
        #Last_end
        remove = 0
        last_end = intervals[0][1]

        #Iterate
        #If last_end < curr_start --> update last_end
        #Else, remove the larger (i.e. use the smaller last end) + Update count
        for start, end in intervals[1:]:
            if last_end <= start:
                last_end = end
            else:
                last_end = min(last_end, end)
                remove += 1
            

        #Return
        return remove