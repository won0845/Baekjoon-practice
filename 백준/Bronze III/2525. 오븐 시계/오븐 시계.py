import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

H, M = map(int, input().split())
cookingTime = int(input())

carryH = cookingTime // 60
remainMin = cookingTime % 60

endHour = H+carryH
endMin = M+remainMin

if endMin >= 60:
    endHour += (endMin//60)
    endMin %= 60

if endHour >= 24:
    endHour %= 24


print(endHour, endMin)