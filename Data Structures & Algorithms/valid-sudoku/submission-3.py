from collections import defaultdict as dd

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Initiate hashsets
        row_set = dd(set)
        col_set = dd(set)
        square_set = dd(set)

        #Iterate through each element
        for i in range(9):
            for j in range(9):
                #Check each element
                #If the element is the special characer ".", move to the next element
                if board[i][j] == ".":
                    continue

                #If  the element exists in sets, return False
                if (board[i][j] in row_set[i] or
                    board[i][j] in col_set[j] or
                    board[i][j] in square_set[(i//3,j//3)]):
                    return False
                #Else add element to sets
                else:
                    row_set[i].add(board[i][j])
                    col_set[j].add(board[i][j])
                    square_set[(i//3,j//3)].add(board[i][j])

        #If not element exists in their respective hashsets, return True
        return True