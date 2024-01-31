import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    lst = []
    cont = 1
    for _ in range(N):
        A, B = map(int, input().split())
        lst.append([A, B])
    lst.sort(key=lambda x: x[0])
    fir = lst[0][1]
    for i in range(len(lst)):
        if fir > lst[i][1]:
            fir = lst[i][1]
            cont += 1
    print(cont)
