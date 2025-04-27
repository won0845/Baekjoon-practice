l = list(map(int,input().split()))
print(sum(map(lambda x:l[0] - x<1001,l)) - 1)