class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        
        #Only continue if 1
        #Look at t, b, l , r
        #Skip when go beyond boarder
        #Implement dfs
        islands = 0
        visited = set()

        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            
            directions = [[-1,0], [1,0], [0,-1], [0,1]]

            while q:
                row, col = q.popleft() #q.pop() makes it dfs

                for dr, dc in directions:
                    dr, dc = row + dr, col + dc

                    if (dr, dc) not in visited and (
                        dr >= 0 and dr < rows and dc >= 0 and dc < cols
                    ) and grid[dr][dc] == "1":
                        visited.add((dr, dc))
                        q.append((dr, dc))


        for r in range(rows):
            for c in range(cols):
               if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r, c)
                islands += 1
        
        return islands