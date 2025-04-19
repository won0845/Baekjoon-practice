N = int(input())
Pasta = input().split()
HyunBin = input().split()

for p in Pasta:
    if p not in HyunBin:
        print(p)
        break
