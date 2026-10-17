class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        grid_set = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue

                #Rows
                if board[r][c] in row_set[r]:
                    return False
                else:
                    row_set[r].add(board[r][c])

                #Cols
                if board[r][c] in col_set[c]:
                    return False
                else:
                    col_set[c].add(board[r][c])

                #Grid
                if board[r][c] in grid_set[r//3][c//3]:
                    return False
                else:
                    grid_set[r//3][c//3].add(board[r][c])


        return True
                