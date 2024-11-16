n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    
    for j in range(b):
        print("X"*a)
    print()
