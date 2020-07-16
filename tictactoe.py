#INITIAL VALUE OF BOARD
board = {'1':' ', '2':' ', '3':' ', 
            '4':' ', '5':' ', '6':' ', 
            '7':' ', '8':' ', '9':' '}

display = board
#DEFAULT INTRO
def intro():
    print("TIC TAC TOE BY ALLIF IZZUDDIN")

    print("\nThis is your board\n")

    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('+++++')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('+++++')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

    print("\nRefer the position as follows: \n")

    print('7' + '|' + '8' + '|' + '9')
    print('+++++')
    print('4' + '|' + '5' + '|' + '6')
    print('+++++')
    print('1' + '|' + '2' + '|' + '3')

#PLAYER BOARD ASSIGNMENT 
def print_board(player,post):
    if player == 1:
        post = str(post)
        board[post] = 'X'
    if player == 2:
        post = str(post)
        board[post] = 'O'
    
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('+++++')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('+++++')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    return board

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
        tic = input('Please mark your board :')
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
    print(tic)
    display.pop(tic)
    print(display)
    return display, tic

#CHECK IF THE MARK IS EXIST
def checkMark(board1,tic):
    checkok = False
    print(board1)
    #tic = str(tic)
    print('The mark is {}'.format(board1[tic]))
    while checkok == False:
        if tic in board1.keys():
            checkok = True
            break
        elif tic not in board1.keys():
            print("The mark already taken")
            break


#CHECK WHO IS THE WINNER
def winner(board,player):
    if (board['7'] == board['4'] and board['7'] == board['1']):
        if board['7'] != ' ' or board['4'] != ' ' or board['1'] != ' ' :      
            print('Player {} WIN\n'.format(player))
            print(board['7'] + '|' + board['8'] + '|' + board['9'])
            print('+++++')
            print(board['4'] + '|' + board['5'] + '|' + board['6'])
            print('+++++')
            print(board['1'] + '|' + board['2'] + '|' + board['3'])

    elif board['7'] == board['5'] and board['7'] == board['3']:
        if board['7'] != ' ' or board['5'] != ' ' or board['3'] != ' ' :
            print('Player {} WIN\n'.format(player))
            print(board['7'] + '|' + board['8'] + '|' + board['9'])
            print('+++++')
            print(board['4'] + '|' + board['5'] + '|' + board['6'])
            print('+++++')
            print(board['1'] + '|' + board['2'] + '|' + board['3'])
    elif (board['7'] == board['8'] and board['7'] == board['9']) :
        if board['7'] != ' ' or board['8'] != ' ' or board['9'] != ' ' :
            print('Player {} WIN\n'.format(player))
            print(board['7'] + '|' + board['8'] + '|' + board['9'])
            print('+++++')
            print(board['4'] + '|' + board['5'] + '|' + board['6'])
            print('+++++')
            print(board['1'] + '|' + board['2'] + '|' + board['3'])
    elif (board['8'] == board['5'] and board['8'] == board['2']) :
        if board['8'] != ' ' or board['5'] != ' ' or board['2'] != ' ' :
            print('Player {} WIN\n'.format(player))
            print(board['7'] + '|' + board['8'] + '|' + board['9'])
            print('+++++')
            print(board['4'] + '|' + board['5'] + '|' + board['6'])
            print('+++++')
            print(board['1'] + '|' + board['2'] + '|' + board['3'])
    elif (board['9'] == board['5'] and board['9'] == board['1']) :
        if board['9'] != ' ' or board['5'] != ' ' or board['1'] != ' ' :
            print('Player {} WIN\n'.format(player))
            print(board['7'] + '|' + board['8'] + '|' + board['9'])
            print('+++++')
            print(board['4'] + '|' + board['5'] + '|' + board['6'])
            print('+++++')
            print(board['1'] + '|' + board['2'] + '|' + board['3'])
    elif (board['9'] == board['6'] and board['9'] == board['3']) :
        if board['9'] != ' ' or board['6'] != ' ' or board['3'] != ' ' :
            print('Player {} WIN\n'.format(player))
            print(board['7'] + '|' + board['8'] + '|' + board['9'])
            print('+++++')
            print(board['4'] + '|' + board['5'] + '|' + board['6'])
            print('+++++')
            print(board['1'] + '|' + board['2'] + '|' + board['3'])
    elif (board['1'] == board['2'] and board['1'] == board['3']) :
        if board['1'] != ' ' or board['2'] != ' ' or board['3'] != ' ' :
            print('Player {} WIN\n'.format(player))
            print(board['7'] + '|' + board['8'] + '|' + board['9'])
            print('+++++')
            print(board['4'] + '|' + board['5'] + '|' + board['6'])
            print('+++++')
            print(board['1'] + '|' + board['2'] + '|' + board['3'])
    else :
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print('+++++')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('+++++')
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        return True, player

def sambung():
    while True:
        cont = input('Do you want to continue? YES or NO :')
        if cont == 'YES':
            game(board)
        else :
            print('SEE YAAA')
            break

def game(board):
    
    game_on = True
    lost = False
    player = 0
    mark = 'X'
    tic = 1
    intro()

    while game_on == True:
        player,mark = marker()
        checkMark(board,tic)
        tic = julat()
        display, tic = position(tic)
        board = print_board(player,tic)
        lost = winner(board,player)
        if lost == True:
            print('Player {} won the game'.format(player))
            game_on = False
            break
        else :
            continue
    return False

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
#intro()
#print_board(1,1)
#marker()
#julat()


# update_board,post = position(8)
# print('\nUpdated board post is {}'.format(update_board))
# print('\nPlayer mark is {}'.format(post))

#problem
#checkMark(update_board,post)

update_board ={'7':'X', '8':'X', '9':' ', 
            '4':'X', '5':' ', '6':' ', 
            '1':'O', '2':' ', '3':'X'}

#print(update_board)

#winner(update_board,1)

#print(type(update_board))

#position(1)

checkMark(update_board,2)