
def wincounter(board, t):
    # 가로줄 판단.
    for row in board:
        if row == [t, t, t]:
            return True
        
    # 세로줄 판단.
    for col in range(3):
        if [board[row][col] for row in range(3)] == [t, t, t]:
            return True
        
    # 대각선 판단.
    if [board[0][0], board[1][1], board[2][2]] == [t, t, t]:
        return True
    if [board[2][0], board[1][1], board[0][2]] == [t, t, t]:
        return True
    
    return False
def solution(board):
    OX = [0,0]
    board = [list(row) for row in board]
    bb = [''.join(row) for row in board]
    b = ''
    for i in bb:
        b += i
    for i in b:
        if i == 'O':
            OX[0] += 1
        elif i == 'X':
            OX[1] += 1
        else:
            continue
    check = OX[0] - OX[1]
    c = [0,1]
    print(wincounter(board, 'X'))
    print(wincounter(board, 'O'))
    if check not in c:
        return 0
    if wincounter(board, 'X') and wincounter(board, 'O'):
        return 0
    if wincounter(board, 'X') and check != 0:
        return 0
    if wincounter(board, 'O') and check != 1:
        return 0
    return 1