'''
CREATED MAINLY FOR REVISING PYTHON SKILLS
BY ALLIF IZZUDDIN BIN ABDULLAH
'''

#INITIAL VALUE OF BOARD
# board = {'1':' ', '2':' ', '3':' ', 
#             '4':' ', '5':' ', '6':' ', 
#             '7':' ', '8':' ', '9':' '}

import sys

board = {'7':' ', '8':' ', '9':' ', 
            '4':' ', '5':' ', '6':' ', 
            '1':' ', '2':' ', '3':' '}

# update_board = {'7':'X', '8':'O', '9':'O', 
#             '4':' ', '5':' ', '6':' ', 
#             '1':' ', '2':' ', '3':' '}

#dummy counter
display = board.copy()

#DEFAULT INTRO
def intro():
    print("TIC TAC TOE BY ALLIF IZZUDDIN")

    print("\nThis is your board\n")

    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('+++++')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('+++++')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

    print("\nRefer the position of marker as follows: \n")

    print('7' + '|' + '8' + '|' + '9')
    print('+++++')
    print('4' + '|' + '5' + '|' + '6')
    print('+++++')
    print('1' + '|' + '2' + '|' + '3')

#PLAYER BOARD ASSIGNMENT 
def print_board(player,post):
    board_print = board.copy()
    if player == 1:
        post = str(post)
        board_print[post] = 'X'
    elif player == 2:
        post = str(post)
        board_print[post] = 'O'
    # print(f'Board print is {board_print}')
    # print(board_print['7'] + '|' + board_print['8'] + '|' + board_print['9'])
    # print('+++++')
    # print(board_print['4'] + '|' + board_print['5'] + '|' + board_print['6'])
    # print('+++++')
    # print(board_print['1'] + '|' + board_print['2'] + '|' + board_print['3'])
    return board_print

#ASSIGN THE PLAYER (1 OR 2)
def marker(player=0, marker='X'):
    while True:
        player = input("Please choose 1 (Player1) or 2 (Player2) :" )
        if player.isdigit() == True:
            player = int(player)
            if player == 1:
                print("\nYou are player 1 with marker X")
                break 
            elif player == 2:
                print('\nYou are player 2 with marker O')
                marker = 'O'
                break
            elif player !=1 or 2:
                print("\nWrong input, please try again")
        else:
            print("\nWrong input, digit only, please try again")
    return player,marker

#CHECK THE TIC RANGE
def julat(tic=0):
    while True:
        tic = input('\nPlease mark your board :')
        if tic.isdigit() == True:
            tic1 = int(tic)
            #print(tic1)
            if tic1 in range(1,10):
                return tic1
                break
            elif tic1 not in range(1,10):
                print("Please key in range 1 to 9")
        else:
            print("Wrong input, digit only")


#REMOVE MARK THAT HAS BEEN TAKEN
def position(tic):
    tic = str(tic)
    #print(tic)
    display_tic = display.copy()
    display_tic.pop(tic)
    x =len(display_tic)
    #print('\n',display,'\n')
    #print(f'Length of the dict is {x}')
    return x

#CHECK IF THE MARK IS EXIST
def checkMark(x,tic):
    board1 = x.copy()
    # print(board1)
    #tic = str(tic)
    #print('The mark is {}'.format(board1[tic]))
    
    if tic in board1.keys() == True:
        pass
    elif tic in board1.keys() == False:
        print("The mark already taken")
        


#CHECK WHO IS THE WINNER
def winner(y,player):
    board1 = y.copy()
    if board1['7'] == board1['4'] == board1['1'] != ' ' :      
        print('Player {} WIN\n'.format(player))
        print(board1['7'] + '|' + board1['8'] + '|' + board1['9'])
        print('+++++')
        print(board1['4'] + '|' + board1['5'] + '|' + board1['6'])
        print('+++++')
        print(board1['1'] + '|' + board1['2'] + '|' + board1['3'])
        return False
    elif board1['7'] == board1['5'] == board1['3'] != ' ' :
        print('Player {} WIN\n'.format(player))
        print(board1['7'] + '|' + board1['8'] + '|' + board1['9'])
        print('+++++')
        print(board1['4'] + '|' + board1['5'] + '|' + board1['6'])
        print('+++++')
        print(board1['1'] + '|' + board1['2'] + '|' + board1['3'])
        return False
    elif board1['7'] == board1['8']  == board1['9'] != ' ' :
        print('Player {} WIN\n'.format(player))
        print(board1['7'] + '|' + board1['8'] + '|' + board1['9'])
        print('+++++')
        print(board1['4'] + '|' + board1['5'] + '|' + board1['6'])
        print('+++++')
        print(board1['1'] + '|' + board1['2'] + '|' + board1['3'])
        return False
    elif board1['8'] == board1['5'] == board1['2'] != ' ' :
        print('Player {} WIN\n'.format(player))
        print(board1['7'] + '|' + board1['8'] + '|' + board1['9'])
        print('+++++')
        print(board1['4'] + '|' + board1['5'] + '|' + board1['6'])
        print('+++++')
        print(board1['1'] + '|' + board1['2'] + '|' + board1['3'])
        return False
    elif board1['9'] == board1['5'] == board1['1'] != ' ' :
        print('Player {} WIN\n'.format(player))
        print(board1['7'] + '|' + board1['8'] + '|' + board1['9'])
        print('+++++')
        print(board1['4'] + '|' + board1['5'] + '|' + board1['6'])
        print('+++++')
        print(board1['1'] + '|' + board1['2'] + '|' + board1['3'])
        return False
    elif board1['9'] == board1['6'] == board1['3'] != ' ' :
        print('Player {} WIN\n'.format(player))
        print(board1['7'] + '|' + board1['8'] + '|' + board1['9'])
        print('+++++')
        print(board1['4'] + '|' + board1['5'] + '|' + board1['6'])
        print('+++++')
        print(board1['1'] + '|' + board1['2'] + '|' + board1['3'])
        return False
    elif board1['1'] == board1['2'] == board1['3'] != ' ' :
        print('Player {} WIN\n'.format(player))
        print(board1['7'] + '|' + board1['8'] + '|' + board1['9'])
        print('+++++')
        print(board1['4'] + '|' + board1['5'] + '|' + board1['6'])
        print('+++++')
        print(board1['1'] + '|' + board1['2'] + '|' + board1['3'])
        return False
    else :
        print(board1['7'] + '|' + board1['8'] + '|' + board1['9'])
        print('+++++')
        print(board1['4'] + '|' + board1['5'] + '|' + board1['6'])
        print('+++++')
        print(board1['1'] + '|' + board1['2'] + '|' + board1['3'])
        return True

def sambung():
    while True:
        cont = input('Do you want to continue? YES or NO :')
        if cont == 'YES':
            game(board)
        else :
            print('SEE YAAA')
            break

#test
'''
def winner1(board,player):
    if board['7'] == board['4']:
        if board['7'] == board['1']:
            print('Player {} win'.format(player))
            print('\nCase 2\n')
            print(board['7'] + '|' + board['8'] + '|' + board['9'])
            print('+++++')
            print(board['4'] + '|' + board['5'] + '|' + board['6'])
            print('+++++')
            print(board['1'] + '|' + board['2'] + '|' + board['3'])
        else:
            print('TEETTTT')
'''
'''
tictactoe = True

while tictactoe == True:
    #main = True
    main_on = game(board)
    if main_on == False:
        sambung()
    else:
        tictactoe = False
        break
'''

def gameplay():
    intro()
    pemain, tanda = marker()
    kira = 10
    for kira in range(1,10):
        
        posisi = julat()
        checkMark(display,posisi)
        board_display = print_board(pemain,posisi)

        if pemain == 1:
            pemain = 2
        elif pemain == 2:
            pemain = 1
        
        final_board = board_display.copy()
        replay = winner(final_board,2)

        if replay == True:
            pass
        elif replay == False:
            return replay
            break

        kira = position(posisi)

game = True
while game == True:
    sambung = gameplay()
    if sambung == False:
        x = input("Do you want continue? Yes/No : ")
        if x == 'Yes':
            continue
        elif x == 'No':
            print("Thank you, See ya again")
            game = False
            sys.exit("BYE BYE!")

'''
https://stackoverflow.com/questions/25905300/modifying-global-dictionary-in-python-within-a-function
https://www.dataquest.io/blog/tutorial-functions-modify-lists-dictionaries-python/

we should use list.copy or dict.copy in order to prevent the variable change globally
'''