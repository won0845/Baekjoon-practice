import sys
input = sys.stdin.readline

a = input().strip()
n = len(a)

substrings = set()

# 모든 가능한 시작점과 끝점에 대해 반복
for i in range(n):
    for j in range(i, n):
        substrings.add(a[i:j+1])

# 결과 출력
print(len(substrings))