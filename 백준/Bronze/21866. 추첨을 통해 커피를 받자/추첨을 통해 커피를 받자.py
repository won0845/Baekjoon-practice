score = [100,100,200,200,300,300,400,400,500]

lst = list(map(int, input().split()))
check = 0

if sum(lst)>=100:
    check = 2

for i in range(9):
    if lst[i] >score[i]:
        check = 1
        break
        
if check == 0:
    print("none")
elif check == 1:
    print("hacker")
elif check == 2:
    print("draw")
