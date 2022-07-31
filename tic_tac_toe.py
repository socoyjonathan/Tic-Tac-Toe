import os

#spots dictionary
spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
         6: "6", 7: "7", 8: "8", 9: "9"}

def draw_board(spots):
    
    board = (f" {spots[1]} | {spots[2]} | {spots[3]}\n"
             f" --------- \n"
             f" {spots[4]} | {spots[5]} | {spots[6]}\n"
             f" --------- \n"
             f" {spots[7]} | {spots[8]} | {spots[9]}")
    
    print(board)
    
def check_turn(turn):

    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'

def check_for_win(spots):
    #handle horizontal cases
    if (spots[1] == spots[2] == spots[3]) \
    or (spots[4] == spots[5] == spots[6]) \
    or (spots[7] == spots[8] == spots[9]):
        return True
    elif (spots[1] == spots[5] == spots[9]) \
    or (spots[3] == spots[5] == spots[7]):
        return True
    else:
        return False

def tic_tac_toe(spots):
    
    playing = True
    turn = 0
    prev_turn = -1
    complete = False
    
    while(playing):
        #reset screen
        os.system('cls' if os.name == 'nt' else 'clear')
        #draw board
        draw_board(spots)
        
        #if invalid turn occured, let player know
        if prev_turn == turn:
            print("Invalid spot selected, please pick another.")
        prev_turn  = turn
        
        #Get input from player
        choice = input(f"Player " + str((turn % 2) + 1) + "'s turn: Pick your spot or press q to quit!")
        if choice == 'q':
            playing = False
        #Check if the player gave a number 1-9
        elif str.isdigit(choice) and int(choice) in spots:
            #Check if the spot has already been taken
            if not spots[int(choice)] in {"X", "O"}:
                #then valid input, update board
                turn += 1
                spots[int(choice)] = check_turn(turn)
        #check if the game has ended (and if someone won)
        if check_for_win(spots):
            playing, complete = False, True
        if turn > 8:
            playing = False
            
    #Print results
    os.system('cls' if os.name == 'nt' else 'clear')
    #draw board one last time
    draw_board(spots)
    
    if complete:
        if check_turn(turn) == 'X':
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")
    else:
        #tie game
        print("No Winner")
        print("Would you like to play again (y/n): ")
        play_again = input()
        
        if play_again == "y":
            tic_tac_toe(spots)

            
    print("Thanks for playing")
    

if __name__ == "__main__":
    
    tic_tac_toe(spots)
    
    
    
