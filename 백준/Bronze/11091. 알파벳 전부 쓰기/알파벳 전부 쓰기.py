import sys
input = sys.stdin.readline
n = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"


for i in range(n):
    answer = []
    a = input()
    for j in alpha:
        if j in a.lower():
            continue
        else:
            answer.append(j)
    if answer:
        print("missing "+"".join(answer))
    else:
        print("pangram")
