DEC = """
intalize a board.
[
["1", "2", "3"]
["4", "5", "6"]
["7", "8", "9"]
]

user a choose number from one to two, and user b as well
dicide who start 

for loop 1, 9:
    if somone won:
        flag_user_won = True
        break
    elif current_num odd:
        starting_player enter x or o
     else:
        second_player enter x or o

if a won:
    announce a won
if b won:
    announce a b
else:
    announce its a tie!
"""

import random

def create_users():

    print("Welcome to Xcircle!")

    print("Eser A, enter your name: ")
    user_a_name = input()

    print("Eser B, enter your name: ")
    user_b_name = input()

    return user_a_name, user_b_name

def create_board(size):
    board = []
    previous = 1
    for i in range(size):
        row = []
        for j in range(size):
            if previous < 10:
                row.append(str(previous) + str(" "))
            else:
                row.append(str(previous))
            previous = previous + 1
        board.append(row)
    return board

def print_board(board):
    for row in board:
        print(row)

def who_is_the_starting_player(user_a, user_b):
    silver_or_gold = ["silver", "gold"]
    x_or_o = ["X", "O"]

    print("Now we are going to decide who starts")

    print(f'{user_a}, Enter "silver" or "gold": ')
    user_a_choice = input()

    user_a_sign = random.choice(x_or_o)
    user_b_sign = ""

    for sign in x_or_o:
        if sign != user_a_sign:
            user_b_sign = sign

    random_choice = random.choice(silver_or_gold)

    if user_a_choice == random_choice:
        print(f"{user_a} is starting!")
        print(f"for {user_a}, you will have the sign {user_a_sign}, and for {user_b}, you will have the sign {user_b_sign}.")
        return user_a, user_b, user_a_sign, user_b_sign

    else:
        print(f"{user_b} is starting!")
        print(f"for {user_b}, you will have the sign {user_b_sign}, and for {user_a}, you will have the sign {user_a_sign}.")
        return user_b, user_a, user_b_sign, user_a_sign

def get_board_length(board):
    length = 0
    for row in board:
        length += len(row)
    return length

def winning_rows(board):
    for row in board:
        is_winning_row = True
        for col_index in range(len(row) - 1):
            if row[col_index] != row[col_index + 1]:
                is_winning_row = False
                break

        if is_winning_row:
            return "row"

    return "not won"

def winning_cols(board):
    for col_index in range(len(board[0])):
        is_winning_col = True
        for row_index in range(len(board) - 1):
            if board[row_index][col_index] != board[row_index + 1][col_index]:
                is_winning_col = False
                break

        if is_winning_col:
            return "coloumns"

    return "not won"

def winning_diagonals(board):

    # up to down
    is_winning_diagonal = True
    for row_ind in range(len(board) - 1):
        if board[row_ind][row_ind] != board[row_ind + 1][row_ind + 1]:
            is_winning_diagonal = False
            break

    if is_winning_diagonal:
        return "diagonals"

    # down to up
    is_winning_diagonal = True
    row_lengths = len(board[0])
    current_position = board[row_lengths - 1][0]
    row_ind_of_next = row_lengths - 2
    col_ind_of_next = 1
    next_position = board[row_lengths - 2][1]
    for i in range(row_lengths - 1):
            if current_position != next_position:
                return "not won"
            if row_ind_of_next - 1 >= 0 and col_ind_of_next + 1 < row_lengths:
                current_position = next_position
                row_ind_of_next -= 1
                col_ind_of_next += 1
                next_position = board[row_ind_of_next][col_ind_of_next]

    return "diagonals"

def winning_postition(board):

    if winning_rows(board) == "row":
        return "row"

    if winning_cols(board) == "coloumns":
        return "coloumns"

    if winning_diagonals(board) == "diagonals":
        return "diagonals"

    return "not won"

def get_signs_by_names(player_dict, beginning_player, second_player, possible_signs):

    keys = list(player_dict.keys())
    for sign in keys:
        if sign == possible_signs[0]:
            if player_dict[sign] == beginning_player:
                return possible_signs[0], possible_signs[1]
            else:
                return possible_signs[1], possible_signs[0]
    return None, None

def play_turn(board, current_player_sign, players_dict):

    print(f"{players_dict.get(current_player_sign)}'s turn")
    print(f"Enter the positon you want {current_player_sign} to be: ")
    position = int(input())
    if position < 10:
        position = str(position) + " "
    else:
        position = str(position)
    board = insert_sign(board, current_player_sign, position)
    return board

def insert_sign(board, current_player_sign, position):
    for row_ind in range(len(board)):
        for col_ind in range(len(board[row_ind])):
            if board[row_ind][col_ind] == position:
                board[row_ind][col_ind] = current_player_sign + " "
                return board
    return board

def start_game(board, board_length, players_dict, beginning_player, second_player,  beginning_player_wins, second_player_wins):

    are_any_winner = False
    beginning_player_sign, second_player_sign = get_signs_by_names(players_dict, beginning_player, second_player, ["X", "O"])

    for turn_number in range(1, board_length + 1):

        current_player_sign = ""

        if turn_number % 2 == 1:
            current_player_sign = beginning_player_sign
            board = play_turn(board, current_player_sign, players_dict)

        else:
            current_player_sign = second_player_sign
            board = play_turn(board, current_player_sign, players_dict)

        print("board status:")
        print_board(board)

        board_position = winning_postition(board)

        if board_position != "not won":
            print(f"{players_dict[current_player_sign]} won by {board_position}")
            if players_dict[current_player_sign] == beginning_player:
                beginning_player_wins += 1
            else:
                second_player_wins += 1
            are_any_winner = True
            break

    if not are_any_winner:

        print("The game ended with a tie.")

    print(f"{players_dict[beginning_player_sign]} has {beginning_player_wins} wins, and {players_dict[second_player_sign]} has {second_player_wins} wins.")
    print(f"{players_dict[beginning_player_sign]} do you want to play again? (yes/no)")
    first_player = input()
    if first_player == "no":
        print("Thank you two for playing!")
        if beginning_player_wins > second_player_wins:
            return f"{players_dict[beginning_player_sign]} is the winner with {beginning_player_wins} wins.!"
        return f"{players_dict[second_player_sign]} is the winner with {second_player_wins} wins.!"

    print(f"{players_dict[second_player_sign]} do you want to play again? (yes/no)")
    second_player = input()
    if second_player == "no":
        print("Thank you two for playing!")
        if beginning_player_wins > second_player_wins:
            return f"{players_dict[beginning_player_sign]} is the winner with {beginning_player_wins} wins.!"
        return f"{players_dict[second_player_sign]} is the winner with {second_player_wins} wins.!"

    board = board = create_board(len(board[0]))
    print("The board look like this: ")
    print_board(board)
    var = start_game(board, board_length, players_dict, players_dict[beginning_player_sign], players_dict[second_player_sign], beginning_player_wins, second_player_wins)
    return var

def main():

    user_a, user_b = create_users()

    print("Enter board size (3 if you want 3 on 3 board, and 4 if you want 4 on 4 board): ")
    size = int(input())

    board = create_board(size)

    print("The board look like this: ")
    print_board(board)

    board_length = get_board_length(board)

    beginning_player, second_player, beginning_player_sign, second_player_sign = who_is_the_starting_player(user_a, user_b)

    players_dict = {beginning_player_sign: beginning_player, second_player_sign: second_player}

    winner = start_game(board, board_length, players_dict, beginning_player, second_player, 0, 0)

    print(winner)

main()