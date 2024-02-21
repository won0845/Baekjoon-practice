a = int(input())
num = 0
b = int(input())
lst = []


for i in range(a, b+1):  # c = 1, 3,  5 , 7
    count = 0
    for k in range(1, i + 1):
        if i % k == 0:
            count += 1
    if count == 2:
        lst.append(i)
        
if lst:  # lst가 비어있지 않다면
    print(sum(lst))
    print(lst[0])
else:
    print(-1)  # 소수가 없는 경우 -1 출력