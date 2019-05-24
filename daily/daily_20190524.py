# n queens problem
# given an nxn board, determine the max number of queens that can be placed safely

# board: 1 = queen, 0 = empty

def is_safe(board, row:int=0, col:int=0) -> bool:
    # check column
    for i in range(len(board)):
        if board[i][col] == 1:
            return False
    # check row
    for i in range(len(board[0])):
        if board[row][i] == 1:
            return False
    # check diagonal
    #?

    for i,j in zip(range(len(board)), range(len(board[0]))):
        print(f'{i}:{j}')

    return True



def main():
    N = 2
    start_col = 0
    board = [[0 for i in range(N)] for j in range(N)]
    board = [[1,0], [0,0]]
    print(is_safe(board, 1, 1))

if __name__ == '__main__':
    main()