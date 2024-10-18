n = int(input())
lst ={}
for i in range(n):
    a, b = input().split()
    lst[b] = a
lst1 = sorted(lst.items())    
print(min(lst1)[1])