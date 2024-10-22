import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    if lst[0]**2 == lst[1]**2+lst[2]**2:
         print(f"Case #{i+1}: YES")
    else:
         print(f"Case #{i+1}: NO")
         