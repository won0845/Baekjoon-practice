n=int(input())

while n!=0:
    num=list(map(int, input().split()))
    max=0
    for i in range(n-2):
        if num[i]+num[i+1]+num[i+2]>max:
            max=num[i]+num[i+1]+num[i+2]
    print(max)
    n=int(input())