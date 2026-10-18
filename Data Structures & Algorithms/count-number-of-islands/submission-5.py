class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ## Practice both DFS and BFS solutions

        #DFS
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        visited = set()
        count = 0

        def dfs(r,c):
            if (r,c) not in visited and 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                visited.add((r,c))

                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r,c-1)
                dfs(r,c+1)


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    count += 1

        return count
