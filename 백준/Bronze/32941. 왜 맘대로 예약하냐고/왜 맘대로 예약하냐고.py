T, X = map(int, input().split())
N = int(input())
result = True  # 모든 조원 참석 가능 여부

for _ in range(N):
    K = int(input())
    A = list(map(int, input().split()))

    if X not in A:
        result = False

if result:
    print("YES")
else:
    print("NO")
