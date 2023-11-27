# Tic-Tac-Toe

# Create the game board
board = [' ' for _ in range(9)]

# Function to display the game board
def display_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check for a win
def check_win():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True
    return False

# Function to check for a tie
def check_tie():
    return ' ' not in board

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board()
        position = int(input("Enter a number (1-9) to place your mark: ")) - 1

        if board[position] == ' ':
            board[position] = current_player
            if check_win():
                display_board()
                print("Congratulations! Player", current_player, "wins!")
                game_over = True
            elif check_tie():
                display_board()
                print("It's a tie!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That position is already filled. Try again.")

# Start the game
play_game()