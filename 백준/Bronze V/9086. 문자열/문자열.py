T = int(input())

for _ in range(T):
    s = str(input())
    print(''.join(map(str, [s[0], s[-1]])))

          