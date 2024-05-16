def solution(board):
    movement = [(0,1), (0,-1), (1,0), (-1,0),
                (1,1), (-1,1), (1,-1), (-1,-1)]
    h = len(board)
    w = len(board[0])
    
    for y in range(h):
        for x in range(w):
            if board[x][y] == 1:
                for dx,dy in movement:
                    if 0 <= (x + dx) < w and 0 <= (y + dy) < h:
                        if board[x+dx][y+dy] != 1:
                            board[x+dx][y+dy] = 2
    answer = 0
    for y in range(h):
        for x in range(w):
            if board[x][y] == 0:
                answer += 1

        
    return answer