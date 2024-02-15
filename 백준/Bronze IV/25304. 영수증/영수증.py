import sys

input = sys.stdin.readline

totalPrice = int(input())
buyNum = int(input())
buyList = []
sumPrice = 0

for _ in range(buyNum):
    price, Num = map(int, input().split())
    sumPrice += price * Num 
    
if totalPrice == sumPrice:
    print("Yes")
else:
    print('No')