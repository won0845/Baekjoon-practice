import sys

input = sys.stdin.readline

N, K = map(int, input().split())
item = list(map(int, input().split()))
ans = 0

hole = []
while item:
    tem = item.pop(0)

    if tem in hole:
        continue

    if len(hole) < N:
        hole.append(tem)
    else:
        change = None
        maximum = -1
        for mt in hole:
            if mt not in item:
                change = mt
                break
            else:
                idx = item.index(mt)
                if idx > maximum:
                    maximum = idx
                    change = mt

        hole[hole.index(change)] = tem
        ans += 1

print(ans)
