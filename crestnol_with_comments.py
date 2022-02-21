
''' this is game of X and O for two players '''
''' это игра в крестики - нолики на двоих '''



# this is Battlefield - output
# вывод поля боя

# "   | 0 | 1 | 2 |
# " 0 | - | - | - |
# " 1 | - | - | - |
# " 2 | - | - | - |

def fld(x):
    print('   | 0 | 1 | 2 |\n')
    for i in range(3):
        print(f' {i} | {x[i][0]} | {x[i][1]} | {x[i][2]} |\n')
   
# this is win and draw combinations check
# проверка на выигрыши и ничьи

def tester(x):
# rows and columns
# строки и столбцы
    for i in range(3):
        if any([(x[i][0] == x[i][1] == x[i][2] != '-'),
                (x[0][i] == x[1][i] == x[2][i] != '-'),
                ]):
            return True
# diagonales
# диагонали
    if any([(x[0][0] == x[1][1] == x[2][2] != '-'),
            (x[0][2] == x[1][1] == x[2][0] != '-')
            ]):
        return True
# draw
# ничья
    elif '-' not in set([*x[0],*x[1],*x[2]]):
        return 'draw'

# this is Interface, this eat everything, give only correct.
# это Интерфейс, он ест всё, принимает только правильное.

def iface(x,y):
    fld(x)
    while True:
# exit
# выход
        try:
            keyboard = input(f'Player {y}, enter coordinates (row col): ')
            if keyboard == 'q':
                print('Goodbye')
                exit()
# RIGHT INPUT:
# ПРАВИЛЬНЫЙ ВВОД:
# 1: True
            turn = list(map(int, keyboard.split(' ')))
            if x[turn[0]][turn[1]] == '-':
                return turn
# 2: False
            else:
                fld(x)
                print('Enter cordinates of empty field')
# LEFT INPUT:
# ОШИБОЧНЫЙ ВВОД:
# 1: Otherss
# 1: Другое
        except ValueError:
            fld(x)
            print('Enter correct coordinates (row col) or "q" for exit game')
            continue
# 2: Didgits
# 2: Цифры
        except IndexError:
            fld(x)
            print('Enter correct coordinates (0 < OR = row, col, < OR = 2)')
            continue

# it is game logic
# это логика игры

def action(x,y):
    while True:
# for any player (X, O)
# Для каждого игрока (X, O)
        for i in y:
# coordinates from ifase turns to Field
# координаты из интерфейса вводятся в поле
            turn = iface(x, i)
            x[turn[0]][turn[1]] = i
# checking win
# проверка на победу
            if tester(x) == 'draw':
                fld(x)
                return('draw')
            elif tester(x):
                fld(x)
                return(i)
            else:
                continue


# this is new game repeater
# это повторитель новой игры.

def relauncher(func):
    do = 'y'
    while do == 'y':
        func()
        do = input('Do you want one more game? (y/n): ')
    print('Goodbye')

# this is the game
# это сама игра

@relauncher
def main():
# HELLO
# ПРИВЕТСТВИЕ
    print('INITIALIZATION OF NEW GAME, enter "q" for exit game')
    print('First coordinate is row number, second is column number')
# MAIN RULES:
# ГЛАВНЫЕ ПРАВИЛА:
# 1. Field and players
# 1. Поле и игроки
    field = [['-']*3,['-']*3,['-']*3]
    players = ['X', 'O']
# 2. Conditions to win or draw
# 2. Условия для победы и ничьей
    winner = action(field, players)
    if winner == 'draw':
        print('DRAW')
    else:
        print(f'Player {winner}, you win!')

