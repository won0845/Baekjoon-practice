def div(x, y, n):
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                div(x, y, n // 2)
                div(x, y + n // 2, n // 2)
                div(x + n // 2, y, n // 2)
                div(x + n // 2, y + n // 2, n // 2)
                return
    if color == 1:
        result[0] += 1
    else:
        result[1] += 1


k = int(input())

paper = []
result = [0, 0]
for i in range(k):
    paper.append(list(map(int, input().split())))

div(0, 0, k)
print(result[1])
print(result[0])