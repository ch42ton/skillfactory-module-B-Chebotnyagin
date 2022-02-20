
''' this is game of X and O for two players '''
''' это игра в крестики - нолики на двоих '''

def fld(x):


# this is Battlefield - output
# вывод поля боя
# "   | 0 | 1 | 2 |
# " 0 | - | - | - |
# " 1 | - | - | - |
# " 2 | - | - | - |


    print('   | 0 | 1 | 2 |\n')
    print(f' 0 | {x[0][0]} | {x[0][1]} | {x[0][2]} |\n')
    print(f' 1 | {x[1][0]} | {x[1][1]} | {x[1][2]} |\n')
    print(f' 2 | {x[2][0]} | {x[2][1]} | {x[2][2]} |\n')
   
def tester(x):

# this is win and draw combinations check
# проверка на выигрыши и ничьи

    if any([(x[0][0] == x[0][1] == x[0][2] != '-'),
            (x[1][0] == x[1][1] == x[1][2] != '-'),
            (x[2][0] == x[2][1] == x[2][2] != '-'),
            (x[0][0] == x[1][0] == x[2][0] != '-'),
            (x[0][1] == x[1][1] == x[2][1] != '-'),
            (x[0][2] == x[1][2] == x[2][2] != '-'),
            (x[0][0] == x[1][1] == x[2][2] != '-'),
            (x[0][2] == x[1][1] == x[2][0] != '-')
            ]):
        return True
    elif '-' not in set([*x[0],*x[1],*x[2]]):
        return 'draw'

def iface(x,y):

# this is Interface, this eat everything. Enter coordinates, or 'q' for exit or EVERYTHING if you want
# это Интерфейс, он ест всё. Вводи координаты или 'q' чтобы выйти, или ЧТО ЗАБЛАГОРАССУДИТСЯ


    fld(x)
    while True:
        try:
            keyboard = input(f'Player {y}, enter coordinates (X Y): ')
            if keyboard == 'q':
                print('Goodbye')
                exit()
            turn = list(map(int, keyboard.split(' ')))
            if x[turn[1]][turn[0]] == '-':
                return turn
            else:
                fld(x)
                print('Enter cordinates of empty field')
        except ValueError:
            fld(x)
            print('Enter correct coordinates (X Y) or "q" for exit game')
            continue
        except IndexError:
            fld(x)
            print('Enter correct coordinates (0 < OR = X, Y, < OR = 2)')
            continue

def action(x,y):

# it is game logic
# это логика игры

    while True:
        for i in y:
            turn = iface(x, i)
            x[turn[1]][turn[0]] = i
            if tester(x) == 'draw':
                fld(x)
                return('draw')
            elif tester(x):
                fld(x)
                return(i)
            else:
                continue

def repeater(func):

# this is new game repeater
# это повторитель новой игры.

    do = 'y'
    while do == 'y':
        func()
        do = input('Do you want one more game? (y/n): ')
    print('Goodbye')

@repeater
def main():

# this is the game
# это сама игра

    print('INITIALIZATION OF NEW GAME, enter "q" for exit game')
    field = [['-']*3,['-']*3,['-']*3]
    players = ['X', 'O']
    winner = action(field, players)
    if winner == 'draw':
        print('DRAW')
    else:
        print(f'Player {winner}, you win!')

