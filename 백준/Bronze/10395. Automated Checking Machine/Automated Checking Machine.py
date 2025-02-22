a = list(map(int, input().split()))
b = list(map(int, input().split()))
flag = True

for i in range(len(a)):
    if a[i] != b[i]:
        flag = flag and True
    else:
        flag = flag and False
if flag:
    print("Y")
else:
    print("N")