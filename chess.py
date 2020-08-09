from tkinter import *

root = Tk()
root.title("Chess")
root.geometry("800x600")

black_Check = False
white_Check = False
check_Mate = False
king_Picked = False

pos_kings = {"white": (7,4), "black": (0,4)}

width_symbol = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
height_symbol = ['8', '7', '6', '5', '4', '3', '2', '1']

board_State = []
chess_Pieces_img = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

chess_Collab = {"pawn": 0, "rook": 1, "knight": 2, "bishop": 3, "queen": 4, "king": 5, "white": 1, "black": 0}
board_Color = ["#B5E1B2", "#84B661"]
WHITE = "white"
BLACK = "black"
game_Width = 600
game_Height = 600

player_Turn = WHITE
available_Move = []
available_Show = []

game_Board = Canvas(root, width=game_Width, height=game_Height, bg="#EBE8BE")
game_Board.pack(side=LEFT)

scroll_Bar = Scrollbar(root)
scroll_Bar.pack(side=RIGHT, fill=Y)

move_List = Listbox(root, width=200, yscrollcommand = scroll_Bar.set)
move_List.pack(side=LEFT)
scroll_Bar.config(command=move_List.yview)

def next_Move():

    global available_Move, board_State, player_Turn, check_Mate

    if player_Turn == WHITE:
        player_Turn = BLACK
    else:
        player_Turn = WHITE

    y = pos_kings[player_Turn][0]
    x = pos_kings[player_Turn][1]

    for i in range(y+1, 8):
        if board_State[i][x]["chess_piece"] != "":
            if board_State[i][x]["color"] != player_Turn and board_State[i][x]["chess_piece"] == ("queen" or "rook"):
                check_Mate = True
                print("hello9")
                return (i, x)
            break

    for i in range(y-1, -1, -1):
        if board_State[i][x]["chess_piece"] != "":
            if board_State[i][x]["color"] != player_Turn and board_State[i][x]["chess_piece"] == ("queen" or "rook"):
                check_Mate = True
                print("hello10")
                return (i, x)
            break

    for i in range(x+1, 8):
        if board_State[y][i]["chess_piece"] != "":
            if board_State[y][i]["color"] != player_Turn and board_State[y][i]["chess_piece"] == ("queen" or "rook"):
                check_Mate = True
                print("hello11")
                return (y, i)
            break
    
    for i in range(x-1, -1, -1):
        if board_State[y][i]["chess_piece"] != "":
            if board_State[y][i]["color"] != player_Turn and board_State[y][i]["chess_piece"] == ("queen" or "rook"):
                check_Mate = True
                print("hello12")
                return (y, i)
            break

    for i in range(1, min(8-x, y+1)):
        if board_State[y-i][x+i]["chess_piece"] != "":
            if board_State[y-i][x+i]["color"] != player_Turn:
                if board_State[y-i][x+i]["chess_piece"] == ("queen" or "bishop") or (board_State[y-i][x+i]["chess_piece"] == "pawn" and i==1):
                    check_Mate = True
                    print("hello13")
                    return
            break

    for i in range(1, min(x+1, 8-y)):
        if board_State[y+i][x-i]["chess_piece"] != "":
            if board_State[y+i][x-i]["color"] != player_Turn:
                if board_State[y+i][x-i]["chess_piece"] == ("queen" or "bishop") or (board_State[y-i][x+i]["chess_piece"] == "pawn" and i==1):
                    check_Mate = True
                    print("hello14")
                    return
            break

    for i in range(1, min(x+1, y+1)):
        if board_State[y-i][x-i]["chess_piece"] != "":
            if board_State[y-i][x-i]["color"] != player_Turn and board_State[y-i][x-i]["chess_piece"] == ("queen" or "bishop"):
                check_Mate = True
                print("hello15")
                return
            break

    for i in range(1, min(8-x, 8-y)):
        if board_State[y+i][x+i]["chess_piece"] != "":
            if board_State[y+i][x+i]["color"] != player_Turn and board_State[y+i][x+i]["chess_piece"] == ("queen" or "bishop"):
                check_Mate = True
                print("hello16")
                return
            break

    for i in range(8):
        coordY = ((int(i/4)>0) and ((i%4>1) and 2 or -2) or ((i%2) and 1 or -1))
        coordX = ((int(i/4)==0) and ((i%4>1) and 2 or -2) or ((i%2) and 1 or -1))
        if y+coordY>-1 and y+coordY<8 and x+coordX>-1 and x+coordX<8:
            if board_State[y+coordY][x+coordX]["chess_piece"] == "knight" and board_State[y+coordY][x+coordX]["color"]!=board_State[y][x]["color"]:
                check_Mate = True
                print("hello"+str(i))
                return

def move_Set(y, x):

    global available_Move, board_State

    chess_Cardinals = [(1, 0),(0, 1),(-1, 0),(0, -1)]
    chess_Diagonals = [(1, 1),(-1, 1),(1, -1),(-1, -1)]

    if board_State[y][x]["chess_piece"] == "pawn":

        if board_State[y][x]["color"] == "black":
            if board_State[y+1][x]["chess_piece"] == "":
                available_Move.append([y+1, x])
                if y == 1 and board_State[y+2][x]["chess_piece"] == "":
                    available_Move.append([y+2, x])
            if x<7 and board_State[y+1][x+1]["chess_piece"]!="" and board_State[y+1][x+1]["color"]=="white":
                available_Move.append([y+1, x+1])
            if x>0 and board_State[y+1][x-1]["chess_piece"]!="" and board_State[y+1][x-1]["color"]=="white": 
                available_Move.append([y+1, x-1])

        if board_State[y][x]["color"] == "white":
            if board_State[y-1][x]["chess_piece"] == "":
                available_Move.append([y-1, x])
                if y == 6 and board_State[y-2][x]["chess_piece"] == "":
                    available_Move.append([y-2, x])
            if x<7 and board_State[y-1][x+1]["chess_piece"]!="" and board_State[y-1][x+1]["color"] == "black":
                available_Move.append([y-1, x+1])
            if x>0 and board_State[y-1][x-1]["chess_piece"]!="" and board_State[y-1][x-1]["color"] == "black": 
                available_Move.append([y-1, x-1])

    elif board_State[y][x]["chess_piece"] == "rook":

        for i in range(4):
            moveY, moveX = chess_Cardinals[i]
            newY, newX = (y, x)
            while newX+moveX>-1 and newX+moveX<8 and newY+moveY>-1 and newY+moveY<8 and board_State[newY+moveY][newX+moveX]["chess_piece"] == "":
                available_Move.append([newY+moveY, newX+moveX])
                newY += moveY
                newX += moveX
            if newX+moveX>-1 and newX+moveX<8 and newY+moveY>-1 and newY+moveY<8 and board_State[newY+moveY][newX+moveX]["color"] != board_State[y][x]["color"]:
                available_Move.append([newY+moveY, newX+moveX])

    elif board_State[y][x]["chess_piece"] == "knight":
        
        for i in range(8):
            moveY = ((int(i/4)>0) and ((i%4>1) and 2 or -2) or ((i%2) and 1 or -1))
            moveX = ((int(i/4)==0) and ((i%4>1) and 2 or -2) or ((i%2) and 1 or -1))
            if y+moveY>-1 and y+moveY<8 and x+moveX>-1 and x+moveX<8:
                if board_State[y+moveY][x+moveX]["chess_piece"]=="" or board_State[y+moveY][x+moveX]["color"]!=board_State[y][x]["color"]:
                    available_Move.append([y+moveY, x+moveX])
    
    elif board_State[y][x]["chess_piece"] == "bishop":

        for i in range(4):
            moveY, moveX = chess_Diagonals[i]
            newY, newX = (y, x)
            while newX+moveX>-1 and newX+moveX<8 and newY+moveY>-1 and newY+moveY<8 and board_State[newY+moveY][newX+moveX]["chess_piece"] == "":
                available_Move.append([newY+moveY, newX+moveX])
                newY += moveY
                newX += moveX
            if newX+moveX>-1 and newX+moveX<8 and newY+moveY>-1 and newY+moveY<8 and board_State[newY+moveY][newX+moveX]["color"] != board_State[y][x]["color"]:
                available_Move.append([newY+moveY, newX+moveX])

    elif board_State[y][x]["chess_piece"] == "queen":

        for i in range(4):
            moveY, moveX = chess_Cardinals[i]
            newY, newX = (y, x)
            while newX+moveX>-1 and newX+moveX<8 and newY+moveY>-1 and newY+moveY<8 and board_State[newY+moveY][newX+moveX]["chess_piece"] == "":
                available_Move.append([newY+moveY, newX+moveX])
                newY += moveY
                newX += moveX
            if newX+moveX>-1 and newX+moveX<8 and newY+moveY>-1 and newY+moveY<8 and board_State[newY+moveY][newX+moveX]["color"] != board_State[y][x]["color"]:
                available_Move.append([newY+moveY, newX+moveX])

        for i in range(4):
            moveY, moveX = chess_Diagonals[i]
            newY, newX = (y, x)
            while newX+moveX>-1 and newX+moveX<8 and newY+moveY>-1 and newY+moveY<8 and board_State[newY+moveY][newX+moveX]["chess_piece"] == "":
                available_Move.append([newY+moveY, newX+moveX])
                newY += moveY
                newX += moveX
            if newX+moveX>-1 and newX+moveX<8 and newY+moveY>-1 and newY+moveY<8 and board_State[newY+moveY][newX+moveX]["color"] != board_State[y][x]["color"]:
                available_Move.append([newY+moveY, newX+moveX])
    
    elif board_State[y][x]["chess_piece"] == "king":

        for i in range(4):
            moveY, moveX = chess_Cardinals[i]
            if x+moveX>-1 and x+moveX<8 and y+moveY>-1 and y+moveY<8 and (board_State[y+moveY][x+moveX]["chess_piece"] == "" or board_State[y+moveY][x+moveX]["color"] != board_State[y][x]["color"]):
                available_Move.append([y+moveY, x+moveX])

        for i in range(4):
            moveY, moveX = chess_Diagonals[i]
            if x+moveX>-1 and x+moveX<8 and y+moveY>-1 and y+moveY<8 and (board_State[y+moveY][x+moveX]["chess_piece"] == "" or board_State[y+moveY][x+moveX]["color"] != board_State[y][x]["color"]):
                available_Move.append([y+moveY, x+moveX])

def display_Move():

    global available_Move, available_Show
    for i in range(len(available_Move)):
        avail_X = available_Move[i][1]
        avail_Y = available_Move[i][0]
        available_Show.append(game_Board.create_oval(45+avail_X*70, 45+avail_Y*70, 65+avail_X*70, 65+avail_Y*70, fill="#A9A9A9", outline=""))

def del_Move():

    global available_Move, available_Show
    for i in range(len(available_Move)):
        game_Board.delete(available_Show[i])
    available_Move = []
    available_Show = []

def setup_chess_Pieces():

    for i in range(8):
        temp = [];
        for j in range(8):
            temp.append({"chess_piece": "", "color": "", "image": ""});
        board_State.append(temp);

    for i in range(8):
        board_State[1][i]["chess_piece"], board_State[1][i]["color"] = ("pawn", BLACK)
        board_State[6][i]["chess_piece"], board_State[6][i]["color"] = ("pawn", WHITE)

    order = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
    for i in range(8):
        board_State[0][i]["chess_piece"], board_State[0][i]["color"] = (order[i], BLACK)
        board_State[7][i]["chess_piece"], board_State[7][i]["color"] = (order[i], WHITE)

    ascending = ["pawn", "rook", "knight", "bishop", "queen", "king"]
    color = [BLACK, WHITE]
    for i in range(2):
        for j in range(6):
            chess_Pieces_img[i][j] = PhotoImage(file="./chess_pic/"+color[i]+"_"+ascending[j]+".png")

def commit_Suicide(row, col):

    global available_Move, player_Turn, pos_kings

    blocking = False
    diffY = row - pos_kings[player_Turn][0]
    diffX = col - pos_kings[player_Turn][1]

    if diffY == 0:

        if diffX < 0:
            for i in range(col+1, pos_kings[player_Turn][1]):
                if board_State[row][i]["chess_piece"] != "":
                    blocking = True
                    break
            print("hello1")
            if not blocking:
                for i in range(col-1,-1,-1):
                    if board_State[row][i]["chess_piece"] != "":
                        if board_State[row][i]["color"] != player_Turn and (board_State[row-i][col+i]["chess_piece"] == "queen" or board_State[row-i][col+i]["chess_piece"] == "rook"):
                            for move in range(len(available_Move)-1, -1, -1):
                                if available_Move[move][0] != row:
                                    available_Move.pop(move)
                        break

        elif diffX > 0:
            for i in range(col-1, pos_kings[player_Turn][1], -1):
                if board_State[row][i]["chess_piece"] != "":
                    blocking = True
                    break
            print("hello2")
            if not blocking:
                for i in range(col+1,8):
                    if board_State[row][i]["chess_piece"] != "":
                        if board_State[row][i]["color"] != player_Turn and (board_State[row-i][col+i]["chess_piece"] == "queen" or board_State[row-i][col+i]["chess_piece"] == "rook"):
                            for move in range(len(available_Move)-1, -1, -1):
                                if available_Move[move][0] != row:
                                    available_Move.pop(move)
                        break

    elif diffX == 0:

        if diffY < 0:
            for i in range(row+1, pos_kings[player_Turn][0]):
                if board_State[i][col]["chess_piece"] != "":
                    blocking = True
                    break
            print("hello3")
            if not blocking:
                for i in range(row-1,-1,-1):
                    if board_State[i][col]["chess_piece"] != "":
                        if board_State[i][col]["color"] != player_Turn and (board_State[row-i][col+i]["chess_piece"] == "queen" or board_State[row-i][col+i]["chess_piece"] == "rook"):
                            for move in range(len(available_Move)-1, -1, -1):
                                if available_Move[move][1] != col:
                                    available_Move.pop(move)
                        break

        elif diffY > 0:
            for i in range(row-1, pos_kings[player_Turn][0], -1):
                if board_State[i][col]["chess_piece"] != "":
                    blocking = True
                    break
            print("hello4")
            if not blocking:
                for i in range(row+1,8):
                    if board_State[i][col]["chess_piece"] != "":
                        if board_State[i][col]["color"] != player_Turn and (board_State[row-i][col+i]["chess_piece"] == "queen" or board_State[row-i][col+i]["chess_piece"] == "rook"):
                            for move in range(len(available_Move)-1, -1, -1):
                                if available_Move[move][1] != col:
                                    available_Move.pop(move)
                        break

    elif abs(diffY) == abs(diffX):

        if diffX*diffY < 0:

            if diffY < 0:
                for i in range(1, diffX):
                    if board_State[row+i][col-i]["chess_piece"] != "":
                        blocking = True
                        break
                print("hello5")
                if not blocking:
                    for i in range(1, min(8-col, row+1)):
                        if board_State[row-i][col+i]["chess_piece"] != "":
                            if board_State[row-i][col+i]["color"] != player_Turn and (board_State[row-i][col+i]["chess_piece"] == "queen" or board_State[row-i][col+i]["chess_piece"] == "bishop"):
                                print(row, col)
                                for move in range(len(available_Move)-1, -1, -1):
                                    if (available_Move[move][0]-row)*(available_Move[move][1]-col) >= 0:
                                        available_Move.pop(move)
                            break

            else:
                for i in range(1, -diffX):
                    if board_State[row-i][col+i]["chess_piece"] != "":
                        blocking = True
                        break
                print("hello6")
                if not blocking:
                    for i in range(1, min(col+1, 8-row)):
                        if board_State[row+i][col-i]["chess_piece"] != "":
                            if board_State[row+i][col-i]["color"] != player_Turn and (board_State[row-i][col+i]["chess_piece"] == "queen" or board_State[row-i][col+i]["chess_piece"] == "bishop"):
                                for move in range(len(available_Move)-1, -1, -1):
                                    if (available_Move[move][0]-row)*(available_Move[move][1]-col) >= 0:
                                        available_Move.pop(move)
                            break

        elif diffX*diffY > 0:

            if diffY < 0:
                for i in range(1, -diffX):
                    if board_State[row+i][col+i]["chess_piece"] != "":
                        blocking = True
                        break
                print("hello7")
                if not blocking:
                    for i in range(1, min(col+1, row+1)):
                        if board_State[row-i][col-i]["chess_piece"] != "":
                            if board_State[row-i][col-i]["color"] != player_Turn and (board_State[row-i][col+i]["chess_piece"] == "queen" or board_State[row-i][col+i]["chess_piece"] == "bishop"):
                                for move in range(len(available_Move)-1, -1, -1):
                                    if (available_Move[move][0]-row)*(available_Move[move][1]-col) <= 0:
                                        available_Move.pop(move)
                            break

            else:
                for i in range(1, diffX):
                    if board_State[row-i][col-i]["chess_piece"] != "":
                        blocking = True
                        break
                print("hello8")
                if not blocking:
                    for i in range(1, min(8-col, 8-row)):
                        if board_State[row+i][col+i]["chess_piece"] != "":
                            if board_State[row+i][col+i]["color"] != player_Turn and (board_State[row-i][col+i]["chess_piece"] == "queen" or board_State[row-i][col+i]["chess_piece"] == "bishop"):
                                for move in range(len(available_Move)-1, -1, -1):
                                    if (available_Move[move][0]-row)*(available_Move[move][1]-col) <= 0:
                                        available_Move.pop(move)
                            break


def board_Display():

    for i in range(8):
        game_Board.create_text(10, 55+i*70, text=height_symbol[i])
        game_Board.create_text(55+i*70, game_Height-10, text=width_symbol[i])
        for j in range(8):
            game_Board.create_rectangle(20+i*70, 20+j*70, 20+(i+1)*70, 20+(j+1)*70, fill=((i*8+j-i)%2==0) and board_Color[0] or board_Color[1], outline="")

    for i in range(8):
        for j in range(8):
            if not board_State[i][j]["chess_piece"]=="":
                img = chess_Pieces_img[chess_Collab[board_State[i][j]["color"]]][chess_Collab[board_State[i][j]["chess_piece"]]]
                board_State[i][j]["image"] = game_Board.create_image(20+j*70, 20+i*70, anchor=NW, image=img)

setup_chess_Pieces()
board_Display()

pickup = False
col, row = (0, 0)

def coord_pickup(e):

    global chess_Pieces_img, player_Turn, board_State, pickup, col, row, king_Picked
    row, col = (int((e.y-20)/70), int((e.x-20)/70))
    if row>=0 and row<8 and col>=0 and col<8:
        if board_State[row][col]["chess_piece"]!="" and board_State[row][col]["color"]==player_Turn:
            row, col = (int(row), int(col))
            move_Set(row, col)
            commit_Suicide(row, col)
            display_Move()
            game_Board.delete(board_State[row][col]["image"])
            img = chess_Pieces_img[chess_Collab[board_State[row][col]["color"]]][chess_Collab[board_State[row][col]["chess_piece"]]]
            board_State[row][col]["image"] = game_Board.create_image(e.x, e.y, image=img)
            pickup = True
            if board_State[row][col]["chess_piece"] == "king":
                king_Picked = True

def move(e):
    
    global chess_Pieces_img, player_Turn, board_State, pickup, col, row
    if pickup:
        game_Board.coords(board_State[row][col]["image"], e.x, e.y)

def coord_drop(e):

    global chess_Pieces_img, player_Turn, board_State, available_Move, pickup, col, row, king_Picked, check_Mate
    if pickup:
        new_imgx = int((e.x-20)/70)
        new_imgy = int((e.y-20)/70)
        if new_imgx>=0 and new_imgx<8 and new_imgy>=0 and new_imgy<8 and (new_imgx!=col or new_imgy!=row) and [new_imgy, new_imgx] in available_Move:
            if board_State[new_imgy][new_imgx]["chess_piece"] != "":
                game_Board.delete(board_State[new_imgy][new_imgx]["image"])
            board_State[new_imgy][new_imgx]["color"] = board_State[row][col]["color"]
            board_State[row][col]["color"] = ""
            board_State[new_imgy][new_imgx]["chess_piece"] = board_State[row][col]["chess_piece"]
            board_State[row][col]["chess_piece"] = ""
            board_State[new_imgy][new_imgx]["image"] = board_State[row][col]["image"]
            board_State[row][col]["image"] = ""
            if king_Picked:
                pos_kings[board_State[new_imgy][new_imgx]["color"]] = (new_imgy, new_imgx)
                king_Picked = False
                print(pos_kings)
            next_Move()
            if check_Mate:
                move_List.insert(END, "checkmate")
        else:
            new_imgx = col
            new_imgy = row
        game_Board.coords(board_State[new_imgy][new_imgx]["image"], new_imgx*70+20, new_imgy*70+20)
        game_Board.itemconfig(board_State[new_imgy][new_imgx]["image"], anchor=NW)
        pickup = False
        del_Move()


game_Board.bind("<Button-1>", coord_pickup)
game_Board.bind("<B1-Motion>", move)
game_Board.bind("<ButtonRelease-1>", coord_drop)

root.mainloop()
