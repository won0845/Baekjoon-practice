y, x = map(int, input().split())
board = []
for _ in range(y):
    board.append(list(input()))

minV = float('inf')  # 최소값 초기화

for i in range(y - 7):
    for j in range(x - 7):
        # 시작 색깔을 'W'와 'B'로 각각 설정하여 두 경우를 모두 검사
        for start in ['W', 'B']:
            cnt = 0
            for a in range(i, i + 8):
                for b in range(j, j + 8):
                    # 현재 칸의 색상
                    current = board[a][b]
                    # (a + b)의 합이 짝수일 때 시작 색과 같아야 하고, 홀수일 때는 다른 색이어야 함
                    if (a + b) % 2 == 0:
                        if current != start:
                            cnt += 1
                    else:
                        if current == start:
                            cnt += 1
            # 최소값 갱신
            minV = min(minV, cnt)

print(minV)