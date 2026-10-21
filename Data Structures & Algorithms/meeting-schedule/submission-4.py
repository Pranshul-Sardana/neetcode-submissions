"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #Handle edge case
        if len(intervals) == 0:
            return True
            
        #Initiate attend all
        attend = True

        #Sort by start time
        intervals.sort(key = lambda x:x.start)

        #Save the end time of first meeting (prev_end_time)
        prev_end_time = intervals[0].end

        #Iterate [1:]
        for item in intervals[1:]:
            #If start time of curr < prev_end_time --> can't attend (return False)
            #else: Update end time
            if item.start < prev_end_time:
                return False
            else:
                prev_end_time = item.end

        #Return True
        return True