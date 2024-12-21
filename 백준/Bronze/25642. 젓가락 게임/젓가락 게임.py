A, B = map(int, input().split())	# 용태(A), 유진(B)
while 1 :
    B += A
    if B >= 5 :
        print('yt')
        break
    A += B
    if A >= 5 :
        print('yj')
        break