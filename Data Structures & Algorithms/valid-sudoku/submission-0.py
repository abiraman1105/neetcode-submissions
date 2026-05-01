class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            map = {}
            for j in range(9):
                key = board[i][j]
                if key == ".": continue
                elif key in map: return False
                else: map[key] = 1
        
        for i in range(9):
            map = {}
            for j in range(9):
                key = board[j][i]
                if key == ".": continue
                elif key in map: return False
                else: map[key] = 1
        
        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                map = {}
                for i in range(3):
                    for j in range(3):

                        key = board[i + row][j + column]
                        if key == ".": continue
                        elif key in map: return False
                        else: map[key] = 1

        return True
