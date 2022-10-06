from tkinter import *
from tkinter import messagebox

class Player():

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.option = StringVar()
        
    def get_option(self):
        return self.option

class GAME_BOARD():

    def __init__(self, board_size):
        self.row_num = board_size
        self.col_num = board_size
        self.board = []
        self.create_skeleton()
        
    def create_skeleton(self):
        for row in range(self.row_num):
            self.board.append([])
            for col in range(self.col_num):
                self.board[row].append(0)  # append empty cell
                
    def reset_board(self):
        for r in range(self.row_num):
            for c in range(self.col_num):
                tile = self.board[r][c]
                tile['text'] = ' '
                tile['bg'] = 'white'
                
    def cell_button(self, row, col):
        return self.board[row][col]

    def full_board_check(self):
        for row in range(self.row_num):
            for col in range(self.col_num):
                if self.board[row][col]['text'] == ' ':
                    return False
        return True
   
class GAME_GUI(GAME_BOARD):
    def __init__(self, board_size):
        super().__init__(board_size)
        # define window and widget variables
        self.WIN = Tk()
        self.WIN_WIDTH = 1200
        self.WIN_HEIGHT = 700
        self.WIN_TITLE = 'SOS'
        self.BUTTON_HEIGHT = 4
        self.BUTTON_WIDTH = 8
        self.R_TURN = 'Red\'s Turn'
        self.B_TURN = 'Blue\'s Turn'
        self.SIMPLE_GAME = 'Simple Game'
        self.GENERAL_GAME = 'General Game'
        self.red_player = Player("red player", "red")
        self.blue_player = Player("blue player", "blue")
        self.current_turn = StringVar()
        self.gametype = ' '
        self.set_r_turn()
        
    def start(self):
        # place window on computer screen, listen for events
        self.WIN.mainloop()
            
    def restart(self):
        self.reset_board()
        self.set_r_turn()

    def gameboard_GUI(self):
        self.WIN.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}")
        self.WIN.title(self.WIN_TITLE)
        
        for r in range(self.row_num):
            for c in range(self.col_num):
                tile = self.board[r][c] = Button(
                    self.WIN, bg="white", text=' ', height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH, command=lambda row1=r, col1=c: self.move(row1, col1))
                tile.grid(row=r, column=c, padx=2, pady=2)
                
        # simple and general game buttons
        simple_game_button = Radiobutton(self.WIN, text='Simple Game', variable=self.gametype,
                                         value=self.SIMPLE_GAME, command=lambda: self.start_simple())
        simple_game_button.grid(row=0, column=self.col_num+2)
        general_game_button = Radiobutton(self.WIN, text='General Game', variable=self.gametype,
                                          value=self.GENERAL_GAME, command=lambda: self.start_general())
        general_game_button.grid(row=0, column=self.col_num+3)
        
        # restart game button
        restart_game_button = Button(
            self.WIN, text='Restart Game', command=lambda: self.restart())
        restart_game_button.grid(row=5, column=self.col_num+3)
        
        # player labels
        red_label = Label(self.WIN, text='Red Player')
        red_label.grid(row=1, column=self.col_num+2)
        blue_label = Label(self.WIN, text='Blue Player')
        blue_label.grid(row=1, column=self.col_num+3, padx=100)
        
        # player S/O radio buttons
        red_S_button = Radiobutton(
            self.WIN, text='S', variable=self.red_player.option, value='S')
        red_S_button.grid(row=2, column=self.col_num+2)
        red_O_button = Radiobutton(
            self.WIN, text='O', variable=self.red_player.option, value='O')
        red_O_button.grid(row=3, column=self.col_num+2)
        blue_S_button = Radiobutton(
            self.WIN, text='S', variable=self.blue_player.option, value='S')
        blue_S_button.grid(row=2, column=self.col_num+3)
        blue_O_button = Radiobutton(
            self.WIN, text='O', variable=self.blue_player.option, value='O')
        blue_O_button.grid(row=3, column=self.col_num+3)
        
        # output of current turn label
        current_turn_text = Label(self.WIN, textvariable=self.current_turn)
        current_turn_text.grid(row=5, column=self.col_num+1)
        
    def start_simple(self):
        self.gametype = self.SIMPLE_GAME
        messagebox.showinfo('Game', self.gametype)
        
    def start_general(self):
        self.gametype = self.GENERAL_GAME
        messagebox.showinfo('Game', self.gametype)
        
    def is_simple(self):
        return self.gametype == self.SIMPLE_GAME
        
    def is_general(self):
        return self.gametype == self.GENERAL_GAME
        
    def move(self, row, col):
        # print('row: ', row, ' col: ', col)
        tile = self.cell_button(row, col)
        if self.gametype == ' ':
            messagebox.showerror('choose gamemode', 'please choose a gamemode')
        elif tile['text'] == 'S' or tile['text'] == 'O':
            messagebox.showerror(
                'tile occupied', 'cannot make a move here - choose another tile')
        elif (self.get_current_turn() == self.R_TURN):
            if self.red_player.option.get() != 'S' and self.red_player.option.get() != 'O':
                messagebox.showerror('choose option', 'player must choose S or O before making a move')
                return None
            tile['text'] = self.red_player.option.get()
            color = self.red_player.color

            if self.is_simple():
                if self.full_board_check():
                    self.restart()
                    return None
                else:
                    self.set_b_turn()

            elif self.is_general():
                if self.full_board_check():
                    self.restart()
                    return None
                else:
                    self.set_b_turn()
                    
        elif (self.get_current_turn() == self.B_TURN):
            if self.blue_player.option.get() != 'S' and self.blue_player.option.get() != 'O':
                messagebox.showerror('choose option', 'player must choose S or O before making a move')
                return None
            tile['text'] = self.blue_player.option.get()
            color = self.blue_player.color

            if self.is_simple():   
                if self.full_board_check():
                    self.restart()
                    return None
                else:
                    self.set_r_turn()

            if self.is_general():
                if self.full_board_check():
                    if self.full_board_check():
                        self.restart()
                    return None
                else:
                    self.set_r_turn()
                        
    def get_current_turn(self):
        return self.current_turn.get()
        
    def set_r_turn(self):
        self.current_turn.set(self.R_TURN)
        
    def set_b_turn(self):
        self.current_turn.set(self.B_TURN)
        
class START_MENU():

    def __init__(self):
        self.WIN_SIZE = Tk()
        self.WIN_SIZE.geometry("400x400")
        self.WIN_SIZE.title("Select Board Size")
        self.record = BooleanVar()
        self.label = Label(self.WIN_SIZE, text="Enter a board size (must be greater than 2)")
        self.label.pack()
        self.enter_size = Entry(self.WIN_SIZE)
        self.enter_size.pack()
        self.start_button = Button(self.WIN_SIZE, height=4, width=10, text="start game", command=lambda:self.start_game())
        self.start_button.pack()
        
    def display_menu(self):
        self.WIN_SIZE.mainloop()
        
    def start_game(self):
        try:
            board_size = self.enter_size.get()
            board_size = int(board_size)
        except ValueError:
            messagebox.showerror(
                'invalid board size', 'enter a valid board size please (number greater than 2)')
            return None
            
        if board_size < 3:
            messagebox.showerror(
                'invalid board size', 'enter a valid board size please (number greater than 2)')
            return None
        else:
            self.WIN_SIZE.destroy()
            game = GAME_GUI(board_size)
            game.gameboard_GUI()
            game.start()
            
if __name__ == '__main__':
    start = START_MENU()
    start.display_menu()
                    
                    
