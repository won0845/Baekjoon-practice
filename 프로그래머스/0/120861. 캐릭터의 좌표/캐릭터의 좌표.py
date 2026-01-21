def solution(keyinput, board):
    x = 0
    y = 0
    key = {"up": [0, 1], "down" : [0, -1], "left" : [-1, 0], "right" : [1, 0]}
    
    for i in keyinput:
        dx, dy = key[i]
        if abs(x + dx) <= board[0] // 2 and abs(y + dy) <= board[1] // 2:
            x += dx
            y += dy
    
    answer = [x, y]
    return answer