N = int(input())
menu = []
for _ in range(N):
    menu.append(int(input()))

M = int(input())
hap = 0
for _ in range(M):
    hap += menu[int(input())-1]

print(hap)
    