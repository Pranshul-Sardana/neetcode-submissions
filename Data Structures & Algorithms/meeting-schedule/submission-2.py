"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
            
        #Sort itnervals by start time
        intervals.sort(key=lambda x:x.start)
        
        end_time = intervals[0].end

        for item in intervals[1:]:
            if item.start < end_time:
                return False
            else:
                end_time = item.end

        return True