import sys
from collections import deque

input = sys.stdin.readline

# 8방향 이동 (가로, 세로, 대각선)
dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]

while True:
    # 지도의 너비(a)와 높이(b) 입력 받기
    a, b = map(int, input().split())
    
    # 종료 조건
    if a == 0 and b == 0:
        break
    
    # 지도 입력 받기
    islandMap = [list(map(int, input().split())) for _ in range(b)]
    
    # 방문 체크 배열
    visited = [[False] * a for _ in range(b)]
    
    cnt = 0  # 섬 개수 초기화
    
    def bfs(start_x, start_y):
        q = deque([(start_x, start_y)])
        visited[start_y][start_x] = True  # 방문 체크

        while q:
            x, y = q.popleft()
            for i in range(8):  # 8방향 탐색
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <= nx < a and 0 <= ny < b:  # 지도 범위 내인지 확인
                    if not visited[ny][nx] and islandMap[ny][nx] == 1:
                        visited[ny][nx] = True  # 방문 처리
                        q.append((nx, ny))
    
    # 전체 지도 탐색
    for i in range(b):
        for j in range(a):
            if islandMap[i][j] == 1 and not visited[i][j]:
                bfs(j, i)  # 섬 탐색 시작
                cnt += 1   # 섬 개수 증가
    
    # 현재 테스트 케이스 결과 출력
    print(cnt)
