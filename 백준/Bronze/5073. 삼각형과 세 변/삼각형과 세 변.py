import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())

while True:
    if a == b == c == 0:
        break
    else:
        sides = sorted([a, b, c])  # 측면 길이를 오름차순으로 정렬
        if sides[2] >= sides[0] + sides[1]:  # 가장 긴 변이 다른 두 변의 합보다 크거나 같으면 삼각형이 될 수 없습니다.
            print("Invalid")
        else:
            if a == b == c:
                print("Equilateral")
            elif a == b or b == c or a == c:
                print("Isosceles")
            else:
                print("Scalene")
    a, b, c = map(int, input().split())