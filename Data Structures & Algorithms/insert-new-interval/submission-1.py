class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        #Initiate output
        res = []

        #Iterate over elements
        for i, item in enumerate(intervals):
            #If it is the first most element, append at the start
            if newInterval[1] < item[0]:
                res.append(newInterval) 
                return res + intervals[i:]
            #If not and non overlapping, add the current element
            elif newInterval[0] > item[1]:
                res.append(item)

        #If overlapping, create a longer range
            else:
                newInterval = [min(item[0], newInterval[0]), max(item[1], newInterval[1])]
        
        res.append(newInterval)

        return res