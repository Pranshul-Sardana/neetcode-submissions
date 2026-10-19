class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Sort the timing by start time
        intervals.sort(key = lambda x: x[0])
        
        #Initate end time and remove_count
        end_time = intervals[0][1]
        remove_count = 0

        #Iterate for each item 
        for item in intervals[1:]:
            #If start of current < end of the previous, increment remove_count
            if item[0] < end_time:
                remove_count += 1
                end_time = min(end_time, item[1])
            else:
                #Remove the interval that ends later (update end time)
                end_time = max(end_time, item[1])
        
        #Return remove_count
        return remove_count