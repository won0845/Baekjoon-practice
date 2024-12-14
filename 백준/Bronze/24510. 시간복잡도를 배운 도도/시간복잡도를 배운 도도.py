n = int(input())
cnt = 0
for i in range(n):
    a = input()
    cnt =  max(a.count("for")+a.count("while"), cnt)

print(cnt)
        