import random
import os.path
import json
random.seed()

def draw_board(board):
    # develop code to draw the board

    print("-" * 11)
    for row in board:
        print(f"| {' |'.join(row)} |")
        print("-" * 11)
    pass

def welcome(board):
    # prints the welcome message
    # display the board by calling draw_board(board)

    print("Welcome to the 'Unbeatable Noughts and Crosses' game.")
    print("The board layout is shown below:")
    draw_board(board)
    pass

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '

    for row in range(len(board)):
        for col in range(len(board[row])):
            board[row][col]=' '
    return board
    
def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col

      while True:
        move=input ("Please choose a cell to put X in, (1-9): ")
        row, col = (int(move) - 1) // 3, (int(move) - 1) % 3

        if 0<=row<=2 and 0<= col <=2 and board[row][col]==' ':
            board[row][col]='X'
            return row,col
        else:
            print ("Invalid slot!! Please try again")
      return row, col
   

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col

    while True:
        row,col=random.randint(0,2), random.randint(0,2)
        if board[row][col] == ' ' :
            board[row][col] = 'O'
            return row, col

def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise

    for row in board:
        if all(cell==mark for cell in row):
            return True
    for col in range(3):
        if all(board[row][col]==mark for row in range(3)):
            return True
        if all(board[i][i] ==mark for i in range(3)):
            return True
        if all(board[i][2-i]==mark for i in range(3)):
            return True
    else:
            return False
    

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise

    for row in board:
        if any(cell== ' ' for cell in row):
            return False
    return True
        
def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    #repeat the loop

    initialise_board(board)
    draw_board(board)
    while True:
        row,col=get_player_move(board)
        draw_board(board)

        if check_for_win(board,'X'):
            print ("You won the game !")
            return 1
            break
        elif check_for_draw(board):
            print("The game is a draw ! ")
            return 0
            break

        row, col = choose_computer_move(board)
        draw_board(board)

        if check_for_win(board,'O'):
            print("Sadly you lose the game !")
            return -1
            break
        elif check_for_draw(board):
            print("The game is a draw ! ")
            return 0
            break
                    
                
def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program

    print("Enter one of the following options:")
    print("1 - Play the game")
    print("2 - Save score in file 'leaderboard.txt'")
    print("3 - Load and display the scores from 'leaderboard.txt'")
    print("q - End the program")
    choice = input("Enter your choice: ")
    return choice


def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders

    if os.path.isfile('leaderboard.txt'):
        with open('leaderboard.txt','r') as f:
            leaders=json.load(f)
        return leaders
    else:
        return{}
    
def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'

    name=input("Enter your name: ")
    leaders = load_scores()
    leaders[name]=score
    with open('leaderboard.txt','w') as f:
        json.dump(leaders,f)
    return



def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader

    sorted_leaders=sorted(leaders.items(),key=lambda x: x[1], reverse=True)
    print ("Scoreboard: ")
    for name, score in sorted_leaders:
        print(f"{name}: {score}")
    pass


