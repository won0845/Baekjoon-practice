import sys

input = sys.stdin.readline

n = int(input())
sum = 0
lst = []

for _ in range(n):
    a=int(input())
    if a !=0:
        lst.append(a)
    else: 
        lst.pop()
       

for i in lst:
    sum += i
    
print(sum)