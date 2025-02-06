a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

sum1 = a1 + (b1 * 2) + (c1 * 3)
sum2 = a2 + (b2 * 2) + (c2 * 3) 

if sum1 == sum2:
    print(0)
elif sum1 > sum2:
    print(1)
else:
    print(2)