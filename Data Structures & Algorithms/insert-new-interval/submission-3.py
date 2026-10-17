class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #What does an overlap mean?

        #Sorted intervals with start_i
        
        #New array: yes
        ret = []


        #Iterate each interval
        #Sort individually or Merge
        #If end < start_i --> append new_interval
        #If start_i < start, end < end_i --> Interval remains same
        #If start_i < start < end_i and end > end_i --> Start merging intervals

        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                ret.append(newInterval)
                return ret + intervals[i:]
            elif newInterval[0] > interval[1]:
                ret.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), 
                                max(newInterval[1], interval[1])]

        ret.append(newInterval)

        return ret
                
