a, b = map(int,input().split())

lst = [i for i in range(1, a+1)]
answer = []
index = b - 1

while lst:
    index %= len(lst)
    answer.append(lst.pop(index))
    index += b - 1

print("<",end="")
print(", ".join(map(str, answer)), end="")
print(">")