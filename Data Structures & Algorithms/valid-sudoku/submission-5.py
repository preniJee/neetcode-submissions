class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".": 
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
                
        box = {i : {j : set() for j in range(3)} for i in range(3)}

        for i in range(9):
            for j in range(9):
                box_row = i // 3
                box_col = j // 3

                if not board[i][j] == ".":
                    if board[i][j] in box[box_row][box_col]:
                        return False
                    else :
                        box[box_row][box_col].add(board[i][j])
        return True
            
        # for i in range(9):
        #     row_i = [num for num in board[i]]
        #     column_i = [board[j][i] for j in range(9)]

        #     row_dup = {}
        #     col_dup = {}
        #     for j in range(len(board)):
        #         if not row_i[j] == "." :
        #             if row_i[j] in row_dup:
        #                 return False
        #             else : 
        #               row_dup[row_i[j]] = row_i[j]

        #         # column
        #         if not column_i[j] == ".":
        #             if column_i[j] in col_dup:
        #                 return False
        #             else :
        #                 col_dup[column_i[j]] = column_i[j]
                
            # Box 
            
            

        
            
           

