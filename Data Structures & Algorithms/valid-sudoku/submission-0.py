class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #we need to validate a sudoku board
        #a valid sudoku board follows these rules:
        #each row must conta nthe digits 1-9 without duplicates
        #each column must contain the digits 1-9 without duplicates
        #and each of the nine 3x3 subboxes of the grid must contain the digits 1-9 without duplicates
        #initialize a set to keep tack fo any seen digits
        #my approach would be to loop through each row
        #if the element in that row is not a .
        #then we check to see fi the digits was already seen in the set
        #if it was we can return false

        #we do the same process for columns ^

        #will nded to validate each sub box after that 
        #so there are 9 rows and 9 columns
        #we start at (0, 0)
        #we loop through 3 rows and 3 columns
        #so first we loop through row 1 - 3
        #we loop thouogh the cols 1-3
        #we then add 3 to cols to move to the next square and repeat
        #if cols become greater than 8 than we add 3 to row 
        #and reset cols
        
        rows = 9
        cols = 9
        for row in range(rows):
            seen = set()
            for col in range(cols):
                if board[row][col] != '.' and board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])
        

        for col in range(cols):
            seen = set()
            for row in range(rows):
                if board[row][col] != '.' and board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])
        
        rows = 0
        cols = 0

        print(rows, cols)

        while rows < 9:
            seen = set()
            for row in range(rows, rows+3):
                for col in range(cols, cols + 3):
                    print(row, col)
                    if board[row][col] != '.' and board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
                
            cols = cols + 3
            if cols > 8:
                rows = rows + 3
                cols = 0
            seen = set()
 
                #row [2] col [2]

                    


        return True

        
