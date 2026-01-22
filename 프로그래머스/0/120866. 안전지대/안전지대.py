def solution(board):
    n = len(board)
    danger = set()
    dirs = [(-1,-1), (-1,0), (-1,1),
            (0,-1),  (0,0),  (0,1),
            (1,-1),  (1,0),  (1,1)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        danger.add((ni,nj))
                        
    return n*n - len(danger)
    
    
    answer = 0
    return answer