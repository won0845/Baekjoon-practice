import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
time = []

for _ in range(N):
    s, e = map(int, input().split())
    time.append((s, e))

time.sort(key=lambda x: (x[1], x[0]))  # 종료 시간 기준으로 정렬

count = 1  # 맨처음은 선택함

end = time[0][1]

for i in range(1, len(time)):
    if end <= time[i][0]:
        count += 1
        end = time[i][1]
print(count)
