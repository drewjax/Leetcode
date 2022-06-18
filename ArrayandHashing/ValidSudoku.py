import collections


def mySolution(board):
    # check rows
    for row in board:
        isIn = []
        for i in row:
            if i != "." and i not in isIn:
                isIn.append(i)
            elif i != "." and i in isIn:
                return False
            else:
                continue
        #print(isIn)
    # check columns and 3x3 board
    squares = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    for rows in range(9):
        isIn2 = []
        for columns in range(9):
            if board[rows][columns] == ".":
                continue
            if (board[rows][columns] in cols[columns] or 
                board[rows][columns] in squares[(rows // 3, columns // 3)]):
                return False
            cols[columns].add(board[rows][columns])
            squares[(rows // 3, columns // 3)].add(board[rows][columns])
    # check each 3x3 square
    return True

def bestSolution(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set) # key = (r /3, c /3)
    
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r // 3, c // 3)]):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
            
    return True

def main():
    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    print(mySolution(board))

if __name__ == "__main__":
    main()