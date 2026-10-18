class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ## Practice both DFS and BFS solutions

        #DFS
        if not grid:
            return None

        rows, cols = len(grid), len(grid[0])

        visited = set()
        count = 0

        def bfs(r,c):
            q = deque()
            q.append([r,c])
            visited.add((r,c))
            
            while q:
                r,c = q.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]


                for dr, dc in directions:
                    dr = dr+r
                    dc = dc+c

                    if (dr,dc) not in visited and 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == "1":
                        q.append([dr,dc])
                        visited.add((dr,dc))


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    count += 1

        return count
