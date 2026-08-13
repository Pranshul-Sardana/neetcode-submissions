class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Get the size of the matrix
        rows, columns = len(matrix), len(matrix[0])

        #Search for the row
        #Initiate top and bottom pointer
        t, b = 0, rows - 1
        #Iterate till the top pointer <= bottom pointer
        while t <= b:
            #Sample to center row index
            c = t+(b-t)//2
            #If the target < left most element in the row, move the bottom pointer up
            if target < matrix[c][0]:
                b = c - 1
            #If the target > right most element in the row, move the top pointer down
            elif target > matrix[c][-1]:
                t = c + 1
            #else, the target is in the row, and move on
            else:
                break

        #If top > bottom, the element doesn't exist. So, return False
        if t > b:
            return False
        
        #Search for the element in the row using a similar logic to above (this is classic binary search)
        #Initiate the pointers
        l, r = 0, columns - 1
        #set up the while loop
        while l <= r:
            #Sample the center_index
            row_c = l + (r-l)//2
            #If target > value at the center_index, move left pointer
            if target > matrix[c][row_c]:
                l = row_c + 1
            #elif target < value at the center_index, move right pointer
            elif target < matrix[c][row_c]:
                r = row_c - 1
            #else, we found the element
            else:
                return True

        #If not found, return False
        return False