class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # Backtracking

        # Initiate rows and cols
        rows, cols = len(board), len(board[0])

        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            # If board out of range return, or i == len(word)
            if (not 0 <= r < rows or not 0 <= c < cols or board[r][c] != word[i]
                or (r,c) in visited):
                return False

            visited.add((r,c))
            
            res = (dfs(r-1, c, i+1) or
                    dfs(r+1, c, i+1) or
                    dfs(r, c-1, i+1) or
                    dfs(r, c+1, i+1)
                    )

            visited.remove((r,c))
            
            return res
            
            
        #Call dfs
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c, 0):
                    return True

        return False