first_lst = []
second_lst = []

for _ in range(3):
    P, Y, S = input().split()
    first_lst.append(int(Y))
    second_lst.append([int(P), S])

first_lst.sort()
second_lst.sort(reverse=True)

first_teamName = ""
second_teamName = ""

for i in range(3):
    first_teamName += str(first_lst[i] % 100)
    second_teamName += second_lst[i][1][0]

print(first_teamName)
print(second_teamName)
