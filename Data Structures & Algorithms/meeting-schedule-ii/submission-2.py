"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #Edge case: No meetings
        if len(intervals) == 0:
            return 0

        #Initate end time list (append first)
        start_times = sorted([item.start for item in intervals])
        end_times = sorted([item.end for item in intervals])
        
        #Initate rooms (max overlaps) and curr
        rooms, curr = 0, 0
        
        #initiate start and end pointers
        s, e = 0, 0

        while s < len(intervals):
            if start_times[s] < end_times[e]:
                curr += 1
                s += 1
            else:
                curr -= 1
                e += 1

            rooms = max(curr, rooms)


        return rooms