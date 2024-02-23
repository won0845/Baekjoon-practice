a, b, c, d, e, f = map(int, input().split())

# a*e - b*d가 0이 아닌 경우에만 유효
if a*e - b*d != 0:
    x = (c*e - b*f) / (a*e - b*d)
    y = (a*f - c*d) / (a*e - b*d)
    print(int(x), int(y))