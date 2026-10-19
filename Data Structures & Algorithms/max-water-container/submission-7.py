class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Two pointers
        #area = min(heights[l], heights[r])*(r-l)
        #More the smaller height

        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            max_area = max(max_area, min(heights[l], heights[r])*(r-l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area