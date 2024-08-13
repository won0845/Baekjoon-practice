j, n = map(int, input().split())
cnt = 0
ans = 0
for i in range(n):
    q = input()
    for k in q:
        if 'A' <= k <= 'Z':
            cnt += 4
        elif 'a' <= k <= 'z' or k.isdecimal():
            cnt += 2
        elif k == " ":
            cnt += 1
    if cnt <= j:
        ans += 1
    cnt = 0

print(ans)