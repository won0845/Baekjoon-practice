n, m = map(int, input().split())
original_s = input()
for _ in range(m):
    postit = input()
    s = list(original_s)
    res = ''
    for p in postit:
        if s == []:
            break 
        else: 
            if p == s[0]:
                res += p
                s.pop(0)
    if res == original_s:
        print('true')
    else:
        print('false')