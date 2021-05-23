theboard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 
'bottom-L': ' ', 'bottom-M': ' ', 'bottom-R': ' '}

def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('_+_+_')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('_+_+_')
    print(board['bottom-L'] + '|' + board['bottom-M'] + '|' + board['bottom-R'])

turn = 'X'

for i in range(9):
    printboard(theboard)
    print('Turn for ' + turn + ". Move on which space?")
    move = input()
    theboard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printboard(theboard)