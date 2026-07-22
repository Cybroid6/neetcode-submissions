class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        s = set()

        for row in board:
            for val in row:
                if val == '.':
                    continue

                if val in s:
                    return False
                
                else:
                    s.add(val)
            s.clear()

        rows = len(board)
        cols = len(board[0])

        for c in range(cols):
            for r in range(rows):
                val = board[r][c]
                if val == '.':
                    continue
                
                if val in s:
                    return False
                else:
                    s.add(val)
            s.clear()

        for box_r in range(3):
            for box_c in range(3):
    
                for r in range(box_r*3, box_r*3+3):
                    for c in range(box_c*3, box_c*3+3):
                        val = board[r][c]
                        if val == '.':
                            continue
                        if val in s:
                            return False
                        else:
                            s.add(val)
                s.clear()
        return True

        