# https://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/

class node:
    def __init__(self, location):
        self.left = None
        self.up = None
        self.right = None
        self.down = None

        

# find shortest path from start to goal on board with walls
# can move up down left right but not through walls

# board with boolean values
# 1 = wall
# 0 = open
# 2 = goal
# 3 = visited
board = [
    [0,1],
    [0,2]
]
# start point
start = [0,0]
# end point
goal = [1,1]

min_possible_answer = abs(goal[0]) + abs(goal[1]) - abs(start[0]) - abs(start[1])
max_possible_answer = len(board) * len(board[0])

# build a min cost matrix working backwards from the goal
#               from left from above from right from below
# goal-1        1           NULL        NULL        NULL
# goal-2        NULL        
shortest_path_matrix = [
    [max_possible_answer, max_possible_answer],
    [max_possible_answer, max_possible_answer],
]
#shortest_path_matrix = [] # start
#for i in range(len(board)):
#    for j in range(len(board[0])):
#        if board[i][j] == 1:
#            shortest_path_matrix[i][j] = 99

#def get_adjacent_tiles(cur_x: int, cur_y: int, max_x: int, max_y: int):
#    adj = []
    # above
    #if 


grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]

def search(x, y):
    if grid[x][y] == 2:
        print('found at %d,%d' % (x, y))
        return True
    elif grid[x][y] == 1:
        print('wall at %d,%d' % (x, y))
        return False
    elif grid[x][y] == 3:
        print('visited at %d,%d' % (x, y))
        return False
    
    print('visiting %d,%d' % (x, y))

    # mark as visited
    grid[x][y] = 3

    # explore neighbors clockwise starting by the one on the right
    if ((x < len(grid)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(grid)-1 and search(x, y+1))):
        return True

    return False

search(0, 0)