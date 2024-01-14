
n = int(input())
lst = []
for i in range(n):
    a, b = input().split()
    lst.append(int(a) + int(b))
for i in lst:
    print(i)
