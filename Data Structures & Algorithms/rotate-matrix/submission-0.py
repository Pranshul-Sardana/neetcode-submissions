class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # Initiate pointers
        l, r = 0, len(matrix) - 1 
        
        # Two pointers (Iterate till l < r)
        while l < r:
            # For r-l positions
            for i in range(r-l):
                t, b = l, r
                # Save topleft
                topLeft = matrix[t][l+i]

                # Move elements clockwise in an anticlockwise order
                matrix[t][l+i] =  matrix[b-i][l]
                
                matrix[b-i][l] =  matrix[b][r-i]
                
                matrix[b][r-i] =  matrix[t+i][r]
                
                matrix[t+i][r] =  topLeft

            l += 1
            r -= 1