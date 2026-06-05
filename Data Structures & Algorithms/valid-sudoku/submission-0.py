class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = True

        row = {k: [] for k in range(9)}
        col = {k: [] for k in range(9)}
        box = {k: [] for k in range(9)}

        i, j = 0, 0
        while i < 9:
            j = 0
            while j < 9:
                if board[i][j] != '.':
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                j += 1
            i += 1
        
        x, y = 0, 0
        while x < 9:
            y = 0  
            while y < 9:
                if board[x][y] != '.':
                    boxIdx = (x // 3) * 3 + (y // 3)
                    box[boxIdx].append(board[x][y])
                y += 1
            x += 1
        
        z = 0
        while z < 9:
            if len(set(row[z])) != len(row[z]) or len(set(col[z])) != len(col[z]) or len(set(box[z])) != len(box[z]):
                res = False
                break
            z += 1

        return res