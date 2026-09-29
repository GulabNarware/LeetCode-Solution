class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        

        # check the 3X3 grid

        for i in range(0,9,3):

            for j in range(0,9,3):

                grid={}

                for row in range(i,i+3):

                    for col in range(j,j+3):

                        if board[row][col].isdigit():
                            if board[row][col] in grid:
                                return False

                            grid[board[row][col]]=1


        #check for a row 

        for r in range(9):
            rows={}
            for c in range(9):
                if board[r][c].isdigit():
                    if board[r][c] in rows:
                        return False

                    rows[board[r][c]]=1


        # for check the columns

        for c in range(9):

            col={}

            for r in range(9):

                if board[r][c].isdigit():
                    if board[r][c] in col:
                        return False

                    col[board[r][c]]=1

        return True





