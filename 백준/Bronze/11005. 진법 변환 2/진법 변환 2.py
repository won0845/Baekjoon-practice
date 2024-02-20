import sys
input = sys.stdin.readline

numbers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split())
remainder = []
quotient = N

while quotient > 0:
    remainder.append(quotient % B)
    quotient = quotient // B


while remainder:
    K = remainder.pop()
    print(numbers[K], end="")
