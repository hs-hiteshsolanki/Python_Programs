import os

ttt_board = [0,1,2,3,4,5,6,7,8]
p1 =[]
p2 = []

wining = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

def display_bord():
    print(ttt_board[0],'|',ttt_board[1],'|',ttt_board[2])
    print("______________")
    print(ttt_board[3],'|',ttt_board[4],'|',ttt_board[5])
    print("______________")
    print(ttt_board[6],'|',ttt_board[7],'|',ttt_board[8])

def win_lose(player_moves):
    for combo in winning_combinations:
            if all(ttt_board[i] == ttt_board[combo[0]] for i in combo):
                return True
        return False
# Check for a draw (no available moves)
if all(isinstance(x, str) for x in ttt_board):
    os.system('clear')
    display_board()
    print("It's a draw!")
    break

def insert_value():
    player1 = ''
    player2 = ''
    p1_select = input("choose a x or o : ")
    while True:
        if p1_select == 'x':
            player1= 'x'
            player2 = 'o'
            print(f"player 1 is choose {player1} or player 2 is {player2} ")
            break
        elif p1_select == 'o':
            player1 = 'o'
            player2 = 'x'
            print(f"player 1 is choose {player1} or player 2 is {player2} ")
            break
        else:
            print("Invalid input")
            continue

    count = 1
    while True:
        if count == 1 :
            os.system('clear')
            display_bord()
            select_index = int(input(f"Player 1 now select a number : "))
            os.system('clear')
            if select_index < len(ttt_board):
                if ttt_board[select_index] != 'x' and ttt_board[select_index] != 'o':
                    # print(ttt_board[select_index])
                    p1.append(ttt_board[select_index])
                    ttt_board[select_index] = player1
                    # print(ttt_board[select_index])
                    # print(p1)
                    if win_lose(p1):
                        os.system('clear')
                        display_bord()
                        print("Player 1 wins!")
                        break
                    count = 2
                    continue
                else:
                    display_bord()
                    print(f"index is already used : {ttt_board[select_index]}")
                    continue
            else:
                print("Invalid move, try again.")
                continue
        elif count == 2:
            #elif player2:
            select_index = int(input(f"Player 2 now select a number : "))
            os.system('clear')
            if select_index <= len(ttt_board):
                if ttt_board[select_index] != 'x' and ttt_board[select_index] != 'o':
                    # print(ttt_board[select_index])
                    p2.append(ttt_board[select_index])
                    ttt_board[select_index] = player2
                    # print(ttt_board[select_index])
                    # print(p1)
                    if win_lose(p2):
                        os.system('clear')
                        display_bord()
                        print("Player 2 wins!")
                    count = 1
                    continue
                else:
                    display_bord()
                    print(f"index is already used : {ttt_board[select_index]}")
                    continue
            else:
                print("input a valid index number")

insert_value()
