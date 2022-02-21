
''' this is game of X and O for two players '''
''' это игра в крестики - нолики на двоих '''




def fld(x):
    print('   | 0 | 1 | 2 |\n')
    for i in range(3):
        print(f' {i} | {x[i][0]} | {x[i][1]} | {x[i][2]} |\n')

def tester(x):
    for i in range(3):
        if any([(x[i][0] == x[i][1] == x[i][2] != '-'),
                (x[0][i] == x[1][i] == x[2][i] != '-'),
                ]):
            return True
    if any([(x[0][0] == x[1][1] == x[2][2] != '-'),
            (x[0][2] == x[1][1] == x[2][0] != '-')
            ]):
        return True
    elif '-' not in set([*x[0],*x[1],*x[2]]):
        return 'draw'

def iface(x,y):
    fld(x)
    while True:
        try:
            keyboard = input(f'Player {y}, enter coordinates (row col): ')
            if keyboard == 'q':
                print('Goodbye')
                exit()
            turn = list(map(int, keyboard.split(' ')))
            if x[turn[0]][turn[1]] == '-':
                return turn
            else:
                fld(x)
                print('Enter cordinates of empty field')
        except ValueError:
            fld(x)
            print('Enter correct coordinates (row col) or "q" for exit game')
            continue
        except IndexError:
            fld(x)
            print('Enter correct coordinates (0 < OR = row, col, < OR = 2)')
            continue

def action(x,y):
    while True:
        for i in y:
            turn = iface(x, i)
            x[turn[0]][turn[1]] = i
            if tester(x) == 'draw':
                fld(x)
                return('draw')
            elif tester(x):
                fld(x)
                return(i)
            else:
                continue

def relauncher(func):
    do = 'y'
    while do == 'y':
        func()
        do = input('Do you want one more game? (y/n): ')
    print('Goodbye')

@relauncher
def main():
    print('INITIALIZATION OF NEW GAME, enter "q" for exit game')
    print('First coordinate is row number, second is column number')
    field = [['-']*3,['-']*3,['-']*3]
    players = ['X', 'O']
    winner = action(field, players)
    if winner == 'draw':
        print('DRAW')
    else:
        print(f'Player {winner}, you win!')

