class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # The potential numbers of paths grow with the distance from the destination
        # Update these counts iteratively

        # Initiate the bottom row
        row = [1]*n

        for i in range(m - 1):
            # Initaite a new row
            newRow = [1]*n
            # For j in columns (reverse order, skip last)
            for j in range(n-2, -1, -1):
                # Update the new row element
                # As j goes in reverse, newRow[j] updates in reverse order
                newRow[j] = newRow[j+1] + row[j]
            # Update row
            row = newRow

        # Return 0th element of the row
        return row[0]