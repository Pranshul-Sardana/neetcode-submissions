class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # BFS way

        # Initiate a seen set
        seen = set()

        # Initiate an island count
        n = 0

        # Get rows and cols count
        rows, cols = len(grid), len(grid[0])

        # Initiate purturbations
        d_loc = [[-1,0], [0,-1], [1,0], [0,1]]

        # double iterate rows and cols
        for row in range(rows):
            for col in range(cols):
                # Continue if element is 0 or in the seen set 
                if grid[row][col] == "0" or (row,col) in seen:
                    continue

                # Increast the island count
                n +=1 
                # Get current location and Initaite a deque 
                q = deque([(row, col)])
                seen.add((row,col))
                            

                # while elements in deque
                while q:
                    # Continue if element is "0" or in the seen set 
                    r, c = q.popleft()

                    ### if grid[r][c] == "0":
                    ###    continue
                    
                    # If bounds are in the matrix size, add it purtabations to the deque
                    for dr, dc in d_loc:
                        dr, dc = r+dr, c+dc
                        
                        if dr in range(rows) and dc in range(cols) and grid[dr][dc] == "1" and (dr,dc) not in seen:
                            seen.add((dr,dc))
                            q.append((dr,dc))
                    
                
        
        # Return island count
        return n