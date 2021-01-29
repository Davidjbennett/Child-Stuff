import IPython

board = [' '] * 9
mark = ['X','O']
player = 1

Win, Draw, Running = 1,-1,0
Game = Running

def checkPosition(x):
    return (board[x] == ' ')

def HorizontalCheck(x):
    return (board[x] != ' ' and board[x] == board[x+1] == board[x+2])

def VerticalCheck():
    return (board[x] != ' ' and board[x] == board[x+3] == board[x+6])

def DiagonalCheck(x,y):
    return (board[x] != ' ' and board[x] == board[x+y] == board[x+[y*2]])

def CheckWin():
    global Game
    if(HorizontalCheck(0) or HorizontalCheck(3) or HorizontalCheck(6)):
        Game = Win
    elif (VerticalCheck VerticalCheck VerticalCheck)



def drawBoard():
    print("1   |2   |3   ")
    print(" %c  | %c  | %c  " % (board[0], board[1], board[2]))
    print("____|____|____")
    print("4   |5   |6   ")
    print(" %c  | %c  | %c  " % (board[3], board[4], board[5]))
    print("____|____|____")
    print("7   |8   |9   ")
    print(" %c  | %c  | %c  " % (board[6], board[7], board[8]))
    print("____|____|____")

while(Game == Running):
    IPython.display.clear_output()
    drawBoard()
    print("Player %d's Turn" % player)
    marks = marks[player - 1]
    choice = int(input("Enter the position you want to draw"))
    if(checkPosition(choice)):
        board[choice] = mark
        player = 3 - player
