from tkinter import *

root = Tk()
root.title("Chess")
root.geometry("600x600")

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

game_Board = Canvas(root, width=game_Width, height=game_Height, bg="#EBE8BE")
game_Board.pack()

def setup_chess_Pieces():

    for i in range(8):
        temp = [];
        for j in range(8):
            temp.append({"pos_x" : i, "pos_y" : j, "chess_piece": "", "color": "", "image": ""});
        board_State.append(temp);

    for i in range(8):
        board_State[1][i]["chess_piece"] = "pawn"
        board_State[1][i]["color"] = BLACK
        board_State[6][i]["chess_piece"] = "pawn"
        board_State[6][i]["color"] = WHITE

    order = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
    for i in range(8):
        board_State[0][i]["chess_piece"] = order[i]
        board_State[0][i]["color"] = BLACK
        board_State[7][i]["chess_piece"] = order[i]
        board_State[7][i]["color"] = WHITE

    ascending = ["pawn", "rook", "knight", "bishop", "queen", "king"]
    color = [BLACK, WHITE]
    for i in range(2):
        for j in range(6):
            chess_Pieces_img[i][j] = PhotoImage(file="./chess_pic/"+color[i]+"_"+ascending[j]+".png")

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
col = 0
row = 0

def coord_pickup(e):

    global chess_Pieces_img, player_Turn, board_State, pickup, col, row
    row = int((e.x-20)/70)
    col = int((e.y-20)/70)
    if not board_State[col][row]["chess_piece"]=="":
        game_Board.delete(board_State[col][row]["image"])
        img = chess_Pieces_img[chess_Collab[board_State[col][row]["color"]]][chess_Collab[board_State[col][row]["chess_piece"]]]
        board_State[col][row]["image"] = game_Board.create_image(e.x, e.y, image=img)
        pickup = True

def move(e):
    
    global chess_Pieces_img, player_Turn, board_State, pickup, col, row
    if pickup:
        game_Board.coords(board_State[col][row]["image"], e.x, e.y)

def coord_drop(e):

    global chess_Pieces_img, player_Turn, board_State, pickup, col, row
    if pickup:
        new_imgx = int((e.x-20)/70)
        new_imgy = int((e.y-20)/70)
        if new_imgx>=0 and new_imgx<8 and new_imgy>=0 and new_imgy<8:
            temp = board_State[col][row]["color"]
            board_State[col][row]["color"] = ""
            board_State[new_imgy][new_imgx]["color"] = temp
            temp = board_State[col][row]["chess_piece"]
            board_State[col][row]["chess_piece"] = ""
            board_State[new_imgy][new_imgx]["chess_piece"] = temp
            temp = board_State[col][row]["image"]
            board_State[col][row]["image"] = ""
            board_State[new_imgy][new_imgx]["image"] = temp
        else:
            new_imgx = row
            new_imgy = col
        game_Board.coords(board_State[new_imgy][new_imgx]["image"], new_imgx*70+20, new_imgy*70+20)
        game_Board.itemconfig(board_State[new_imgy][new_imgx]["image"], anchor=NW)
        pickup = False


game_Board.bind("<Button-1>", coord_pickup)
game_Board.bind("<B1-Motion>", move)
game_Board.bind("<ButtonRelease-1>", coord_drop)

root.mainloop()
