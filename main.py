import random as r
import sys

def create_table():
    global M
    M = []
    x = None
    y = None
    for i in range(4):
        temp=[]
        for j in range(4):
            x = str(i)
            y = str(j)
            if i == 0:
                temp.append(y)
            elif j == 0:
                temp.append(x)
            else:
                temp.append('-')
        M.append(temp)

def show_table(M):
    for i in range(4):
        print(*M[i], sep=' ')

def check_table(M):
    k = 0
    for i in range(4):
        for j in range(4):
            if M[i][j] == '-':
                k += 1
            else:
                k += 0
    if k == 0:
        sys.exit('Игра окончена!')

def entering_coordinates(M):
    global x , y
    x, y = map(int, input('Введите значения x и y:').split())
    while ((x < 1 or x > 3) or (y < 1 or y > 3)) or M[x][y] != '-':
        x , y = map(int, input('Введите значения x и y:').split())
    else:
        M[x][y] = 'X'
    show_table(M)

def opponent_entering(M):
    X = int(r.randint(1, 3))
    Y = int(r.randint(1, 3))
    while M[X][Y] != '-':
        X = int(r.randint(1,3))
        Y = int(r.randint(1,3))
    else:
        M[X][Y] = 'O'
    show_table(M)

def check_player(M):
    if M[1][1] == M[1][2] == M[1][3] == 'X' or M[2][1] == M[2][2] == M[2][3] == 'X' or M[3][1] == M[3][2] == M[3][3] == 'X' or M[1][1] == M[2][2] == M[3][3] == 'X' or M[1][3] == M[2][2] == M[3][1] == 'X':
        sys.exit('Победа!')
    elif M[1][1] == M[2][1] == M[3][1] == 'X' or M[1][2] == M[2][2] == M[3][2] == 'X' or M[1][3] == M[2][3] == M[3][3] == 'X':
        sys.exit('Победа!')
    else:
        pass

def check_bot(M):
    if M[1][1] == M[1][2] == M[1][3] == 'O' or M[2][1] == M[2][2] == M[2][3] == 'O' or M[3][1] == M[3][2] == M[3][3] == 'O' or M[1][1] == M[2][2] == M[3][3] == 'O' or M[1][3] == M[2][2] == M[3][1] == 'O':
        sys.exit('Ты проиграл!')
    elif M[1][1] == M[2][1] == M[3][1] == 'O' or M[1][2] == M[2][2] == M[3][2] == 'O' or M[1][3] == M[2][3] == M[3][3] == 'O':
        sys.exit('Ты проиграл!')
    else:
        pass

def main():
    n = 1
    create_table()
    show_table(M)
    while n < 5:
        entering_coordinates(M)
        show_table(M)
        check_player(M)
        check_table(M)
        opponent_entering(M)
        show_table(M)
        check_bot(M)
        check_table(M)

main()