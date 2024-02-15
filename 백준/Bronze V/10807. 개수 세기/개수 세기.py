import sys
input = sys.stdin.readline

N = int(input())

listNum = list(map(int, input().split()))
findNum = int(input())
print(listNum.count(findNum))