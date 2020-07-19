from tkinter import *

root = Tk()
root.title("Chess")
root.geometry("600x600")

width_symbol = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
height_symbol = ['8', '7', '6', '5', '4', '3', '2', '1']
chess_pos = []

board_State = [(0, 0)]
chess_Pieces_img = [0, 0, 0, 0, 0]
board_Color = ["#B5E1B2", "#84B661"]
WHITE = "white"
BLACK = "black"
game_Width = 600
game_Height = 600

player_Turn = WHITE

game_Board = Canvas(root, width=game_Width, height=game_Height, bg="#EBE8BE")
game_Board.pack()

def setup_Board():
    for i in range(8):
        game_Board.create_text(10, 55+i*70, text=height_symbol[i])
        game_Board.create_text(55+i*70, game_Height-10, text=width_symbol[i])
        for j in range(8):
            game_Board.create_rectangle(20+i*70, 20+j*70, 20+(i+1)*70, 20+(j+1)*70, fill=((i*8+j-i)%2==0) and board_Color[0] or board_Color[1], outline="")
for i in range(8):
    temp = [];
    for j in range(8):
        temp.append({"pos_x" : "", "pos_y" : "", "chess_piece" : ""});
    chess_pos.append(temp);
chess_pos[1][1]["pos_x"] = 100;
print(chess_pos)
def board_Display():
    pass

setup_Board()
board_Display()
<<<<<<< HEAD

imgx = 20
imgy = 20
pickup = False
chess_Pieces_img[0] = PhotoImage(file="c:/Users/admin/Desktop/python-prj/pawn.png")
chess_pieces = game_Board.create_image(imgx, imgy, anchor=NW, image=chess_Pieces_img[0])

def coord_pickup(e):

    global chess_Pieces_img, player_Turn, imgx, imgy, pickup
    if e.x>imgx and e.x<imgx+70 and e.y>imgy and e.y<imgy+70:
        chess_Pieces_img[0] = PhotoImage(file="c:/Users/admin/Desktop/python-prj/pawn.png")
        chess_pieces = game_Board.create_image(e.x, e.y, image=chess_Pieces_img[0])
        pickup = True

def move(e):
    
    global chess_Pieces_img, player_Turn, pickup
    if pickup:
        chess_Pieces_img[0] = PhotoImage(file="c:/Users/admin/Desktop/python-prj/pawn.png")
        chess_pieces = game_Board.create_image(e.x, e.y, image=chess_Pieces_img[0])

def coord_drop(e):

    global chess_Pieces_img, player_Turn, imgx, imgy, pickup
    if pickup:
        chess_Pieces_img[0] = PhotoImage(file="c:/Users/admin/Desktop/python-prj/pawn.png")
        new_imgx = int((e.x-20)/70)*70+20
        new_imgy = int((e.y-20)/70)*70+20
        if new_imgx>=20 and new_imgx<580 and new_imgy>=20 and new_imgy<580:
            imgx = new_imgx
            imgy = new_imgy
        chess_pieces = game_Board.create_image(imgx, imgy, anchor=NW, image=chess_Pieces_img[0])
        pickup = False


game_Board.bind("<Button-1>", coord_pickup)
game_Board.bind("<B1-Motion>", move)
game_Board.bind("<ButtonRelease-1>", coord_drop)

root.mainloop()
