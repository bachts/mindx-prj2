from tkinter import *

root = Tk()
root.title("Chess")
root.geometry("600x600")

width_symbol = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
height_symbol = ['8', '7', '6', '5', '4', '3', '2', '1']

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

def board_Display():
    pass

setup_Board()
board_Display()


root.mainloop()
