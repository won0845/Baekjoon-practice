while True:
    A, B, C = map(str, input().split())
    B = int(B)
    C = int(C)
    if A == '#' and B == 0 and C == 0:
        break
    if B > 17 or C >= 80:
        print(A, "Senior")
    else:
        print(A, "Junior")