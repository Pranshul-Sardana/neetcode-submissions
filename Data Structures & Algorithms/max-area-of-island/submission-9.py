class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #DFS solution

        rows, cols = len(grid), len(grid[0])

        #Track visited
        #Track max area
        visited = set()
        max_area = 0

        #Implement dfs
        def dfs(r,c):
            if not ((r,c) not in visited and 0<=r<rows and 0<=c<cols and grid[r][c] == 1):
                return 0
            
            visited.add((r,c))

            return (1 + dfs(r-1,c) +
                    dfs(r+1,c) +
                    dfs(r,c-1) +
                    dfs(r,c+1))
        

        #Iterate
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))

        #Return
        return max_area

