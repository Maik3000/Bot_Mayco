"""
[Module] Tic-tac-toe bot utilities.
"""
from random import randint
import requests
from urllib.parse import unquote


API_URL = "http://127.0.0.1:8000"


def is_registry_open() -> bool:
    """
    Checks if registry is available via API.
    """
    try:
        url = "{}/registry".format(API_URL)
        res = requests.get(url)

        if res.text == "true":
            return True
        elif res.text == "false":
            return False

    except:
        return False


def register_user(name: str) -> str:
    """
    Registers user in API game.
    """
    url = "{}/register_player/{}".format(API_URL, name)
    res = requests.post(url)
    player_id = res.text[1]
    return player_id


def is_my_turn(player_id: str) -> bool: 
    """
    Checks if it is our turn via API.
    """
    url = "{}/turn/{}".format(API_URL, player_id)
    res = requests.get(url)
    
    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def read_board() -> list:
    """
    Gets game board via API.
    """
    url = "{}/board".format(API_URL)
    res = requests.get(url)
    board_str = res.text
    board = [
        [board_str[1], board_str[2], board_str[3]], 
        [board_str[4], board_str[5], board_str[6]], 
        [board_str[7], board_str[8], board_str[9]]
    ]

    return board


def decide_move(board: list, player_id: str) -> [int, int]:
    """
    Decides next move to make.
    """
    
    #strategy 
    #ataque

    while player_id == "X":
        
        if board[0][0] == board[0][1] == board[0][2] == board[1][0] == board[1][1] == board[1][2] == board[2][0] == board[2][1] == board[2][2] == "-":
            row = 1
            column = 1

        
        #valuar posibles victorias
        #row 0
        elif board[0][0] == board[0][1] == player_id and board[0][2] == "-":
            row = 0
            column = 2
            
        elif board[0][0] == board[0][2] == player_id and board[0][1] == "-":
            row = 0
            column = 1
            
        elif board[0][1] == board[0][2] == player_id and board[0][0] == "-":
            row = 0
            column = 0

        #row 1
        elif board[1][0] == board[1][1] == player_id and board[1][2] == "-":
            row = 1
            column = 2
            
        elif board[1][0] == board[1][2] == player_id and board[1][1] == "-":
            row = 1
            column = 1
            
        elif board[1][1] == board[1][2] == player_id and board[1][0] == "-":
            row = 1
            column = 0

        #row 2
        elif board[2][0] == board[2][1] == player_id and board[2][2] == "-":
            row = 2
            column = 2

        elif board[2][0] == board[2][2] == player_id and board[2][1] == "-":
            row = 2
            column = 1
            
        elif board[2][1] == board[2][2] == player_id and board[2][0] == "-":
            row = 2
            column = 0

        #line 0
        elif board[0][0] == board[1][0] == player_id and board[2][0] == "-":
            row = 2
            column = 0
            
        elif board[0][0] == board[2][0] == player_id and board[1][0] == "-":
            row = 1
            column = 0

        elif board[1][0] == board[2][0] == player_id and board[0][0] == "-":
            row = 0
            column = 0

        #line 1
        elif board[0][1] == board[1][1] == player_id and board[2][1] == "-":
            row = 2
            column = 1

        elif board[0][1] == board[2][1] == player_id and board[1][1] == "-":
            row = 1
            column = 1
            
        elif board[1][1] == board[2][1] == player_id and board[0][1] == "-":
            row = 0
            column = 1
            
        #line 2
        elif board[0][2] == board[1][2] == player_id and board[2][2] == "-":
            row = 2
            column = 2

        elif board[0][2] == board[2][2] == player_id and board[1][2] == "-":
            row = 1
            column = 2

        elif board[1][2] == board[2][2] == player_id and board[0][2] == "-":
            row = 0
            column = 2

        #diagonal_left
        elif board[0][0] == board[1][1] == player_id and board[2][2] == "-":
            row = 2
            column = 2

        elif board[0][0] == board[2][2] == player_id and board[1][1] == "-":
            row = 1
            column = 1
            
        elif board[1][1] == board[2][2] == player_id and board[0][0] == "-":
            row = 0
            column = 0

        #diagonal_right
        elif board[0][2] == board[1][1] == player_id and board[2][0] == "-":
            row = 2
            column = 0

        elif board[0][2] == board[2][0] == player_id and board[1][1] == "-":
            row = 1
            column = 1
            
        elif board[1][1] == board[2][0] == player_id and board[0][2] == "-":
            row = 0
            column = 2
            
        else:
            #estrategia esquinas
            #par row 0
            if board[0][0] or board[0][2] == "-":
                row = 0 
                column = randint(0,2)
            
                if board[0][0] == "-":
                    row = 0
                    column = 0

                elif board[0][2] == "-":
                    row = 0
                    column = 2

            #par row 2    
            elif board[2][0] or board[2][2] == "-":
                row = 2 
                column = randint(0,2)

                if board[2][0] == "-":
                    row = 2
                    column = 0

                elif board[2][2] == "-":
                    row = 2
                    column = 2
        
        #par column 0
            elif board[0][0] or board[2][0] == "-":
                row = randint(0,2) 
                column = 0

                if board[0][0] == "-":
                    row = 0
                    column = 0

                elif board[2][0] == "-":
                    row = 2
                    column = 0
        
        #par column 2
            elif board[0][2] or board[2][2] == "-":
                row = randint(0,2) 
                column = 2

                if board[0][2] == "-":
                    row = 0
                    column = 2

                elif board[2][2] == "-":
                    row = 2
                    column = 2

            else:
                row = randint(0,2)
                column = randint(0,2)
        return [row, column]    
        
    #defensa
    while player_id == "O":

        #respuesta a opciones de victoria

        #row 0
        if board[0][0] == board[0][1] == player_id and board[0][2] == "-":
            row = 0
            column = 2
            
        elif board[0][0] == board[0][2] == player_id and board[0][1] == "-":
            row = 0
            column = 1
            
        elif board[0][1] == board[0][2] == player_id and board[0][0] == "-":
            row = 0
            column = 0

        #row 1
        elif board[1][0] == board[1][1] == player_id and board[1][2] == "-":
            row = 1
            column = 2
            
        elif board[1][0] == board[1][2] == player_id and board[1][1] == "-":
            row = 1
            column = 1
            
        elif board[1][1] == board[1][2] == player_id and board[1][0] == "-":
            row = 1
            column = 0

        #row 2
        elif board[2][0] == board[2][1] == player_id and board[2][2] == "-":
            row = 2
            column = 2

        elif board[2][0] == board[2][2] == player_id and board[2][1] == "-":
            row = 2
            column = 1
            
        elif board[2][1] == board[2][2] == player_id and board[2][0] == "-":
            row = 2
            column = 0

        #line 0
        elif board[0][0] == board[1][0] == player_id and board[2][0] == "-":
            row = 2
            column = 0
            
        elif board[0][0] == board[2][0] == player_id and board[1][0] == "-":
            row = 1
            column = 0

        elif board[1][0] == board[2][0] == player_id and board[0][0] == "-":
            row = 0
            column = 0

        #line 1
        elif board[0][1] == board[1][1] == player_id and board[2][1] == "-":
            row = 2
            column = 1

        elif board[0][1] == board[2][1] == player_id and board[1][1] == "-":
            row = 1
            column = 1
            
        elif board[1][1] == board[2][1] == player_id and board[0][1] == "-":
            row = 0
            column = 1
            
        #line 2
        elif board[0][2] == board[1][2] == player_id and board[2][2] == "-":
            row = 2
            column = 2

        elif board[0][2] == board[2][2] == player_id and board[1][2] == "-":
            row = 1
            column = 2

        elif board[1][2] == board[2][2] == player_id and board[0][2] == "-":
            row = 0
            column = 2

        #diagonal_left
        elif board[0][0] == board[1][1] == player_id and board[2][2] == "-":
            row = 2
            column = 2

        elif board[0][0] == board[2][2] == player_id and board[1][1] == "-":
            row = 1
            column = 1
            
        elif board[1][1] == board[2][2] == player_id and board[0][0] == "-":
            row = 0
            column = 0

        #diagonal_right
        elif board[0][2] == board[1][1] == player_id and board[2][0] == "-":
            row = 2
            column = 0

        elif board[0][2] == board[2][0] == player_id and board[1][1] == "-":
            row = 1
            column = 1
            
        elif board[1][1] == board[2][0] == player_id and board[0][2] == "-":
            row = 0
            column = 2

        #-------------------------------------------------------------

        #validar bloqueo
        #row 0
        if board[0][0] == board[0][1] == "X" and board[0][2] == "-":
            row = 0
            column = 2
            
        elif board[0][0] == board[0][2] == "X" and board[0][1] == "-":
            row = 0
            column = 1
            
        elif board[0][1] == board[0][2] == "X"  and board[0][0] == "-":
            row = 0
            column = 0

        #row 1
        elif board[1][0] == board[1][1] == "X"  and board[1][2] == "-":
            row = 1
            column = 2
            
        elif board[1][0] == board[1][2] == "X" and board[1][1] == "-":
            row = 1
            column = 1
            
        elif board[1][1] == board[1][2] == "X" and board[1][0] == "-":
            row = 1
            column = 0

        #row 2
        elif board[2][0] == board[2][1] == "X" and board[2][2] == "-":
            row = 2
            column = 2

        elif board[2][0] == board[2][2] == "X" and board[2][1] == "-":
            row = 2
            column = 1
            
        elif board[2][1] == board[2][2] == "X" and board[2][0] == "-":
            row = 2
            column = 0

        #line 0
        elif board[0][0] == board[1][0] == "X" and board[2][0] == "-":
            row = 2
            column = 0
            
        elif board[0][0] == board[2][0] == "X" and board[1][0] == "-":
            row = 1
            column = 0

        elif board[1][0] == board[2][0] == "X" and board[0][0] == "-":
            row = 0
            column = 0

        #line 1
        elif board[0][1] == board[1][1] == "X" and board[2][1] == "-":
            row = 2
            column = 1

        elif board[0][1] == board[2][1] == "X" and board[1][1] == "-":
            row = 1
            column = 1
            
        elif board[1][1] == board[2][1] == "X" and board[0][1] == "-":
            row = 0
            column = 1
            
        #line 2
        elif board[0][2] == board[1][2] == "X" and board[2][2] == "-":
            row = 2
            column = 2

        elif board[0][2] == board[2][2] == "X" and board[1][2] == "-":
            row = 1
            column = 2

        elif board[1][2] == board[2][2] == "X" and board[0][2] == "-":
            row = 0
            column = 2

        #diagonal_left
        elif board[0][0] == board[1][1] == "X" and board[2][2] == "-":
            row = 2
            column = 2

        elif board[0][0] == board[2][2] == "X" and board[1][1] == "-":
            row = 1
            column = 1
            
        elif board[1][1] == board[2][2] == "X" and board[0][0] == "-":
            row = 0
            column = 0

        #diagonal_right
        elif board[0][2] == board[1][1] == "X" and board[2][0] == "-":
            row = 2
            column = 0

        elif board[0][2] == board[2][0] == "X" and board[1][1] == "-":
            row = 1
            column = 1
            
        elif board[1][1] == board[2][0] == "X" and board[0][2] == "-":
            row = 0
            column = 2
               
        else:
            row = randint(0,2)
            column = randint(0,2)
        return [row, column]

def validate_move(board: list, move: list) -> bool:
    """
    Checks if the desired next move hits an empty position.
    """
    row, col = move[0], move[1]

    if board[row][col] == "-":
        return True

    return False


def send_move(player_id: str, move: list) -> None:
    """
    Sends move to API.
    """
    row, col = move[0], move[1]
    url = "{}/move/{}/{}/{}".format(API_URL, player_id, row, col)
    res = requests.post(url)
    return None


def does_game_continue() -> bool:
    """
    Checks if the current match continues via API.
    """
    url = "{}/continue".format(API_URL)
    res = requests.get(url)

    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def print_board(board: list) -> None:
    '''
    Prints the baord in console to watch the game.
    '''
    print("\nCurrent board: \n")
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("----------")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("----------")
    print(board[2][0], "|", board[2][1], "|", board[2][2], "\n")
