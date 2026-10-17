class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Sort by the start
        intervals.sort(key = lambda x:x[0])

        #new arr
        new_arr = [intervals[0]]

        #Iterate
        #If prev_end >= curr_start --> update previous with current end
        #else, append new
        for interval in intervals[1:]:
            if new_arr[-1][1] >= interval[0]:
                new_arr[-1][1] = max(new_arr[-1][1], interval[1])
            else:
                new_arr.append(interval)
            
        #Return
        return new_arr
