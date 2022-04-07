# tic tac toe

from re import X
from turtle import shape


grid = [[" "," "," "],[" "," "," "],[" "," "," "]]

def draw():
    for i in range(3):
        print("{0} | {1} | {2}".format(grid[i][0],grid[i][1],grid[i][2]))

def move(shape):
    valid_move = False

    while (not valid_move):
        x = int(input("{0} row: ".format(shape)))
        y = int(input("{0} col: ".format(shape)))

        if (x >= 0 and x < 3 and y >= 0 and y < 3):
            if (grid[x][y] == " "):
                grid[x][y] = shape
                valid_move = True
            else:
                print("illegal move!")
        else:
            print("illegal move!")
    return shape,x,y
        
def check_win(move):
    shape = move[0]
    x = move[1]
    y = move[2]

    win_row = [shape,shape,shape]
    row = [grid[x][0],grid[x][1],grid[x][2]]
    col = [grid[0][y],grid[1][y],grid[2][y]]
    diag1 = [grid[0][0],grid[1][1],grid[2][2]]
    diag2 = [grid[0][2],grid[1][1],grid[2][0]]

    if (win_row in [row,col,diag1,diag2]):
        return True
    else:
        return False
        
def game():
    round = 1
    turn = 0
    shapes = ["x","o"]
    draw()
    not_over = True

    while (not_over and round <= 9):
        not_over =  not check_win(move(shapes[turn]))
        draw()
        turn = 1 - turn
        round += 1

    if (not_over):
        print("tie!")
    else:
        print(shapes[turn], "wins!")

game()
    

