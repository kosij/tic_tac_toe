# tic tac toe

grid = [[" "," "," "],[" "," "," "],[" "," "," "]]

def draw():
    for i in range(3):
        print("{0} | {1} | {2}".format(grid[i][0],grid[i][1],grid[i][2]))

def move(shape,x,y):
    if (x >= 0 and x < 3 and y >= 0 and y < 3):
        if (grid[x][y] == " "):
            grid[x][y] = shape
        else:
            print("illegal move!")
    else:
        print("illegal move!")
        
def check_win(shape,x,y):
    win_row = [shape,shape,shape]
    row = [grid[x][0],grid[x][1],grid[x][2]]
    col = [grid[0][y],grid[1][y],grid[2][y]]
    diag1 = [grid[0][0],grid[1][1],grid[2][2]]
    diag2 = [grid[0][2],grid[1][1],grid[2][0]]

    if (win_row in [row,col,diag1,diag2]):
        print(shape, "wins!")
        return True
    else:
        return False
        
def game():
    turn = 0
    shapes = ["x","o"]
    draw()
    not_over = True
    while (not_over):
        #ask user for row and column
        row = int(input("{0} row: ".format(shapes[turn])))
        col = int(input("{0} col: ".format(shapes[turn])))
        move(shapes[turn],row,col)
        draw()
        not_over =  not check_win(shapes[turn],row,col)
        turn = 1 - turn

game()
    

