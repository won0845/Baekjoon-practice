import sys

input = sys.stdin.readline

string = input().rstrip()
splt = input().rstrip()
stk = []

for i in string:
    stk.append(i)
    if i == stk[-1] and "".join(stk[len(stk)-len(splt):]) == splt:
        del stk[len(stk)-len(splt):]

if stk:
    print("".join(stk))
else:
    print("FRULA")
