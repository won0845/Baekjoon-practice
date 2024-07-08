import sys
input = sys.stdin.readline
n= int(input())

for i in range(n):
    year = int(input())
    N = year % 100
    if (year+1) % N == 0:
        print("Good")
    else:
        print("Bye")