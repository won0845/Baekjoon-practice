n = int(input())

for i in range(n):
    lst = list(map(int,input().split()))
    print(f"Case #{i+1}: {max(lst)}")