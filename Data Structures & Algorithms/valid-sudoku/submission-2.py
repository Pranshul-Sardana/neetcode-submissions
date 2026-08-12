class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        column_dict = defaultdict(set)
        square_dict = defaultdict(set)
        
        #Checking rows
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in row_dict[i] or
                    board[i][j] in column_dict[j] or
                    board[i][j] in square_dict[(i//3, j//3)]                    
                   ):
                    return False
                row_dict[i].add(board[i][j])
                column_dict[j].add(board[i][j])
                square_dict[(i//3, j//3)].add(board[i][j])
                    
        return True