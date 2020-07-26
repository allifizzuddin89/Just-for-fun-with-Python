'''
CREATED MAINLY FOR REVISING PYTHON SKILLS
BY ALLIF IZZUDDIN BIN ABDULLAH
'''

#INITIAL VALUE OF BOARD
# board = {'1':' ', '2':' ', '3':' ', 
#             '4':' ', '5':' ', '6':' ', 
#             '7':' ', '8':' ', '9':' '}

import sys
import copy

board = {'7':' ', '8':' ', '9':' ', 
            '4':' ', '5':' ', '6':' ', 
            '1':' ', '2':' ', '3':' '}

board_print = board.copy()

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
    print(board_print)
    print(type(board_print))

    #had to change post type to str, else it will append a new tuples instead of update the value of the dict
    #anything inside dict tuples is str
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
def julat(player,tic=0):
    while True:
        tic = input(f'\nPlayer {player} mark your board :')
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
    display_tic = board_print.copy()
    display_tic.pop(tic)
    x =len(display_tic)
    #print('\n',display,'\n')
    #print(f'Length of the dict is {x}')
    return x

#CHECK IF THE MARK IS EXIST
def checkMark(x,tic):
    # print(board1)
    #tic = str(tic)
    #print('The mark is {}'.format(board1[tic]))
    
    if tic in x.keys() == True:
        pass
    elif tic in x.keys() == False:
        print("The mark already taken")
        


#CHECK WHO IS THE WINNER
def winner(y,player):
    board1 = y
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
    elif board1['1'] == board1['2'] == board1['3'] == board1['4'] == board1['5'] == board1['6'] == board1['7'] == board1['8'] == board1['9'] != ' ' :
        print(board1['7'] + '|' + board1['8'] + '|' + board1['9'])
        print('+++++')
        print(board1['4'] + '|' + board1['5'] + '|' + board1['6'])
        print('+++++')
        print(board1['1'] + '|' + board1['2'] + '|' + board1['3'])
        return True
    else :
        print('Player {} WIN\n'.format(player))
        print(board1['7'] + '|' + board1['8'] + '|' + board1['9'])
        print('+++++')
        print(board1['4'] + '|' + board1['5'] + '|' + board1['6'])
        print('+++++')
        print(board1['1'] + '|' + board1['2'] + '|' + board1['3'])
        return False

def sambung():
    while True:
        cont = input('Do you want to continue? YES or NO :')
        if cont == 'YES':
            game(board)
        else :
            print('SEE YAAA')
            break



def gameplay():
    intro()
    pemain, tanda = marker()
    board_print = board.copy()
    for x in range(1,10):        
        posisi = julat(pemain)
        checkMark(board_print,posisi)
        board_print = print_board(pemain,posisi)

        if pemain == 1:
            pemain = 2
        elif pemain == 2:
            pemain = 1
        
        print(board_print)
        # final_board = board_display.copy()
        replay = winner(board_print,pemain)

        if replay == True:
            print('GAME OVER')
            pass
        elif replay == False:
            return replay
            break

        position(posisi)
    #print('GAME OVER')
    return False

game = True
while game == True:
    sambung = gameplay()
    if sambung == False:
        x = input("Do you want continue? Yes/No : ")
        if x == 'Yes':
            board_print = board.copy()
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