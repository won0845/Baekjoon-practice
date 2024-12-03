n = int(input())
for i in range(n):
    lst = input().split()
    lst.reverse()
    print(f"Case #{i+1}:",end=" ")
    print(*lst)