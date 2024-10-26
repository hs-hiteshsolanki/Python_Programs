import os

import click

ttt_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
wining = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
player1 = ''
player2 = ''

def display_bord(player1,player2):
    print(f"player 1 is choose {player1} or player 2 is {player2} ")

    print(ttt_board[0], '|', ttt_board[1], '|', ttt_board[2])
    print("__________")
    print(ttt_board[3], '|', ttt_board[4], '|', ttt_board[5])
    print("__________")
    print(ttt_board[6], '|', ttt_board[7], '|', ttt_board[8])

def win_lose():
    if all(items == 'x' or items == 'o' for items in ttt_board):
        print(f'match is draw')
        return True
    for moves in wining:
        if ttt_board[moves[0]] == 'x' and ttt_board[moves[1]] == 'x' and ttt_board[moves[2]] == 'x':
            print("player X wining")
            return True
        elif ttt_board[moves[0]] == 'o' and ttt_board[moves[1]] == 'o' and ttt_board[moves[2]] == 'o':
            print("player O wining")
            return True
    return False

def insert_value():
    while True:
        x_o_select = input("choose a player 1 (x or o) : ")
        if x_o_select.lower() == 'x':
            player1 = 'x'
            player2 = 'o'
            # print(f"player 1 is choose {player1} or player 2 is {player2} ")
            break
        elif x_o_select.lower() == 'o':
            player1 = 'o'
            player2 = 'x'
            # print(f"player 1 is choose {player1} or player 2 is {player2} ")
            break
        else:
            print("Invalid input")
            continue

    count = 1
    while True:
        if count == 1:
            # os.system('clear')
            display_bord(player1,player2)
            # select_index_player1 = int(input(f"Player 1 now select a number : "))
            select_index_player1 = click.prompt("Player 1 now select a number ", type=int)
            select_index_player1 = select_index_player1 - 1
            if select_index_player1 <= len(ttt_board):
                if ttt_board[select_index_player1] != 'x' and ttt_board[select_index_player1] != 'o':
                    print(ttt_board[select_index_player1])
                    ttt_board[select_index_player1] = player1
                    os.system('clear')
                    if win_lose() == True:
                        display_bord(player1,player2)
                        break
                    count = 2
                    continue
                else:
                    os.system('clear')
                    print(f"index is already used : {ttt_board[select_index_player1]}")
                    continue
            else:
                print("Player choose wrong move")
                continue
        elif count == 2:
            display_bord(player1,player2)
            select_index_player2 = click.prompt("Player 2 now select a number ", type=int)
            # select_index_player2 = int(input(f"Player 2 now select a number : "))
            select_index_player2 = select_index_player2 - 1
            if select_index_player2 <= len(ttt_board):
                if ttt_board[select_index_player2] != 'x' and ttt_board[select_index_player2] != 'o':
                    ttt_board[select_index_player2] = player2
                    os.system('clear')
                    if win_lose() == True:
                        # os.system('clear')
                        display_bord(player1,player2)
                        break
                    count = 1
                    continue
                else:
                    os.system('clear')
                    print(f"index is already used : {ttt_board[select_index_player2]}")
                    continue
            else:
                print("Player choose wrong move")
                continue

insert_value()
