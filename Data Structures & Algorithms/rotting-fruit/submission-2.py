class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        rotten = deque()
        healthy = 0
        #Find rotten. T = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append([r,c])
                elif grid[r][c] == 1:
                    healthy += 1

        #Run simulation
        #Every time step, get directions. If fruit exists. Make rotten.
        t = 0
        while healthy > 0:
            t += 1
            if t == rows*cols:
                return -1
            len_rotten = len(rotten)
            for i in range(len_rotten):
                rot_r, rot_c = rotten.popleft()
                directions = [[rot_r-1, rot_c], [rot_r, rot_c-1], 
                                [rot_r+1, rot_c], [rot_r, rot_c+1]]
                for dr, dc in directions:
                    if 0<=dr<rows and 0<=dc<cols and grid[dr][dc] == 1:
                        grid[dr][dc] = 2
                        rotten.append([dr,dc])
                        healthy -= 1
            
        return t

