class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Set up two pointers and initiate heights
        l, r = 0, len(heights) - 1
        l_height, r_height, area = 0, 0, 0
        
        #Set up our loops
        while l < r:
            #print(f"{l = }, {heights[l] = }, {l_height = }, {r = }, {heights[r] = }, {r_height = }")
            
            #Check if the new heights are greater than the previous heights
            if heights[l] >= l_height:
                l_height = heights[l]
            else:
                l += 1
                continue

            if heights[r] >= r_height:
                r_height = heights[r]
            else:
                r -= 1
                continue

            #Check if the new area is greater
            new_area = (r - l )*min(l_height, r_height)
            #print(f"{l = }, {r = }, {r - l = }, {l_height = }, {r_height = }, {new_area = }")
            if new_area > area:
                area = new_area

            #Increment the pointer
            if r_height < l_height:
                r -= 1
            else:
                l += 1

        return area