n = int(input())
lst = 0
for i in range(n):
    a = input()
    if a == "anj":
        lst = 1
if lst == 1:
    print("뭐야;")
elif lst == 0:
    print("뭐야?")
    