

def display_game(table):
    print(" ---+---+---")
    print(f" {table[0][0]} | {table[0][1]} | {table[0][2]}   /   1 | 2 | 3")
    print(f" {table[1][0]} | {table[1][1]} | {table[1][2]}   /   4 | 5 | 6")
    print(f" {table[2][0]} | {table[2][1]} | {table[2][2]}   /   7 | 8 | 9")
    print(" ---+---+---")

def convert_selection(selection):
    match selection:
        case 1:
            return (0,0)
        case 2: 
            return (0,1)
        case 3:
            return (0, 2)
        case 4:
            return (1, 0)
        case 5: 
            return (1, 1)
        case 6:
            return (1, 2)
        case 7:
            return (2, 0)
        case 8:
            return (2, 1)
        case 9: 
            return (2, 2)

        
def mark_position(selection, table, value):
    row, col = convert_selection(selection)
    table[row][col] = value
       

def check_valid_option(selection, table):
    row, col = convert_selection(selection)
    position_value = table[row][col]
    
    if position_value == " ":
        return True
    else:
        return False
def check_valid_options(table):
    for row in table:
        for col in row:
            if col == " ":
                return True
    return False
    
def check_game_status(table):
    top_row = table[0]
    mid_row = table[1]
    bot_row = table[2]

    if top_row[0] == top_row[1] == top_row[2] != " ":
        return True, top_row[0]
    elif mid_row[0] == mid_row[1] == mid_row[2] != " ":
        return True, mid_row[0]
    elif bot_row[0] == bot_row[1] == bot_row[2] != " ":
        return True, bot_row[0]
    elif top_row[0] == mid_row[0] == bot_row[0] != " ":
        return True, top_row[0]
    elif top_row[1] == mid_row[1] == bot_row[1] != " ":
        return True, top_row[1]
    elif top_row[2] == mid_row[2] == bot_row[2] != " ":
        return True, top_row[2]
    elif top_row[0] == mid_row[1] == bot_row[2] != " ":
        return True, top_row[0]
    elif top_row[2] == mid_row[1] == bot_row[0] != " ":
        return True, top_row[2]
    else:
        return False, None
    

def select_position(table):
    if not check_valid_options(table):
        return False
    
    selection_flag = True
    selection = 0
    while selection_flag:
        selection = int(input("Select a position to play: "))
        if selection >= 1 and selection <=  9:
            if check_valid_option(selection, table):
                selection_flag = False
            else:
                print("Position already marked!")
        else:
            print("Invalid option!")
            continue
    
    return selection 


def mark_player_selection(table, player_number, signal):
    print(f"Player {player_number} turn:")
    selection = select_position(table)
    if selection:
        mark_position(selection, table, signal)
    else:
        return False
    
    
def tic_tac_toe():
    table = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
   
    flag = 0
    while flag <=9:
        print("+------------ Tic Tac Toe ------------+")
        display_game(table)
        mark_player_selection(table, 1, "X")
        mark_player_selection(table, 2, "O")
        
        game_status, winner = check_game_status(table)

        if game_status:
            print(f"Game over! {winner} won!")
            return 

      
        display_game(table)
        flag += 1
    
    print("Game over! It's a draw!")

tic_tac_toe()