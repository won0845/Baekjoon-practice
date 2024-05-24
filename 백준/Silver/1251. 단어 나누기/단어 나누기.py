n = input().strip()
dic = []

for i in range(len(n)-2):
    for j in range(i+1, len(n)-1):
        a = n[:i+1]
        b = n[i+1:j+1]
        c = n[j+1:]
        dic.append("".join([a[::-1],b[::-1],c[::-1]]))
dic.sort()
print(dic[0])