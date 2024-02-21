import sys

input = sys.stdin.readline

A = int(input())
while A != -1:

    div = []

    for i in range(1, A + 1):
        if A % i == 0:
            div.append(i)

    k = div.pop()
    if sum(div) == k:
        print("{} =".format(k), end=" ")
        pcnt = 0
        for i in range(len(div)):
            print("{}".format(div[i]), end="")
            pcnt += 1
            if pcnt < len(div):
                print(" + ", end="")
        print()
    else:
        print("{} is NOT perfect.".format(k))
    A = int(input())