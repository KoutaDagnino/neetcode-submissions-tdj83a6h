class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row=[s for s in board[i] if s!="."]
            if len(set(row))!=len(row):
                return False
            col=[r[i] for r in board if r[i]!="."]
            if len(set(col))!=len(col):
                return False
        for i in range(3):
            for j in range(3):
                sub_board = [board[3*i+x//3][3*j+x%3] for x in range(9)]
                square=[s for s in sub_board if s!="."]
                if len(set(square))!=len(square):
                    return False
        return True