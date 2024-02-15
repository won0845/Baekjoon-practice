import sys

input = sys.stdin.readline

V1, V2, V3 = map(int, input().split())

sameCount = 0

if V1 == V2:
    if V2 == V3:
        sameCount = 3
        print(10000 + (V1 * 1000))
    elif V2 != V3:
        sameCount = 2
        print(1000+( V1 * 100))

elif V1 != V2:
    if V2 == V3:
        sameCount = 2
        print(1000 + (V2 * 100))
    elif V1 == V3:
        sameCount = 2
        print(1000 + (V1 * 100))
    elif V2 != V3:
        sameCount = 1
        if V1> V2:
            if V1> V3:
                print(V1*100)
            else:
                print(V3*100)
        else:
            if V2>V3:
                print(V2*100)
            else:
                print(V3*100)

