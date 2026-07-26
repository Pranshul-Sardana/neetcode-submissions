class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Initialize 2 points and max area
        l, r = 0, len(height) - 1
        max_h_l, max_h_r = height[l], height[r]
        max_area = 0

        while l < r:
            # Choose the pointer
            if max_h_l <= max_h_r:
                l += 1 # Move the smaller pointer
                max_h_l = max(max_h_l, height[l]) # Update the max height
                max_area += max_h_l - height[l] # Add area (will already be 0 or greater)
                #print(f"{l = }, {max_h_l = }, {height[l] = }, {max_area = }")
            else:
                r -= 1 # Update pointer
                max_h_r = max(max_h_r, height[r]) # Update max height
                max_area += max_h_r - height[r] # Add area (will already be 0 or greater)
                #print(f"{r = }, {max_h_r = }, {height[r] = }, {max_area = }")
            
        return max_area