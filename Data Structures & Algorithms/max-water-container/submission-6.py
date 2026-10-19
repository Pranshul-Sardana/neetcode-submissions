class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Two pointer
        #area = min(heights[l], heights[r])*(r-l)
        #If not, computer area, check max(max_area, area)

        #Initiate pointers and variables
        l, r = 0, len(heights) - 1
        max_area = 0

        #Iterate
        while l < r:
            max_area = max(max_area, min(heights[l], heights[r])*(r-l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r-=1
            
        #Return
        return max_area