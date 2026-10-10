class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Start the output list
        res = []
        
        #Iterate elements
        for i, item in enumerate(intervals):
            #If the end of newInterval is before the start of element, then add the newInterval
            if newInterval[1] < item[0]:
                res.append(newInterval)
                return res + intervals[i:]
            #else if the start of newInterval is before the end of element, then add the element
            elif newInterval[0] > item[1]:
                res.append(item)
            #else, merge the elements
            else:
                newInterval = [min(newInterval[0], item[0]), max(newInterval[1], item[1])]

        res.append(newInterval)

        return res
