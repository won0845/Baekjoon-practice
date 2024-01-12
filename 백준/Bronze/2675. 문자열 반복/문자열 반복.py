a = int(input())

for i in range(a):
    a, S = input().split()
    for k in S:
        print(int(a)*k,end="")
    print()
