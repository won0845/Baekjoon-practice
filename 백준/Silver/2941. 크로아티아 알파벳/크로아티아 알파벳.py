import sys

input = sys.stdin.readline
inputS = input().strip()

char_cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in char_cro:
    inputS= inputS.replace(i,"*")
print(len(inputS))