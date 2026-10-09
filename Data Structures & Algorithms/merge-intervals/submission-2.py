class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #Sort the intervals
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        #print(intervals[0])

        #Put the 0th element in the starting array.

        res = [intervals[0]]

        #Iterate through rsest
        for item in intervals[1:]:
            #If the element starts before the previous one ends, merge
            if item[0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], item[1])]
            #Else append
            else:
                res.append(item)

        return res