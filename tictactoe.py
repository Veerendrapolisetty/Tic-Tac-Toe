board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
current_player = "X"
game = True
winner = None

def display_board(board):
    print(board[0] + " | " + board[1] + " | "+ board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | "+ board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | "+ board[8])

def user_input(board):
    global current_player
    inp = int(input("Eneter num between 1 to 9: "))
    if inp <= 9 and inp > 0 and board[inp-1] == "-":
        board[inp-1] = current_player
        switch_player()
    else:
        print("Select a valid input num")
        return False

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def check_Hor(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
        
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
        
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False
        
def check_ver(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
        
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
        
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False
        
def check_dia(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
        
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False
        
def check_winner(board):
    global game
    if check_Hor(board) or check_ver(board) or check_dia(board):
        print(f"Winner is {winner}!")
        game = False
    return False
def check_tie(board):
    global game
    if "-" not in board:
        print("Game is tied")
        game = False
    return False

while game:
    display_board(board)
    user_input(board)
    if check_winner(board):
        print(board)
        break
    if check_tie(board):
        print(board)
        break



