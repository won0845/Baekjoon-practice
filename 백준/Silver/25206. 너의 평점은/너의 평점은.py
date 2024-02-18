# import sys
#
# input = sys.stdin.readline
#
# char_cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
#
# inputS = input().strip()
# count = 0
# check_char = len(inputS)
#
# for i in char_cro:
#     if i in inputS:
#         s = inputS.split(i)
#         if (len(i) == 1 for i in s):
#             break
#         inputS = "".join(s)
#         check_char -= len(i)
#         count += 1
#
# print(check_char + count)

# ## 이렇게 쉬운 문제를
# import sys
#
# input = sys.stdin.readline
# inputS = input().strip()
#
# char_cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
#
# for i in char_cro:
#     inputS= inputS.replace(i,"*")
# print(len(inputS))

import sys

input = sys.stdin.readline
A = 0
cnt = 0
k = 0
for _ in range(20):
     # 과목평점

    a, b, c = map(str, input().split())
    b = float(b)
    if c == "A+":
        k = 4.5
        cnt += b
    elif c == "A0":
        k = 4.0
        cnt += b
    elif c == "B+":
        k = 3.5
        cnt += b
    elif c == "B0":
        k = 3.0
        cnt += b
    elif c == "C+":
        k = 2.5
        cnt += b
    elif c == "C0":
        k = 2.0
        cnt += b
    elif c == "D+":
        k = 1.5
        cnt += b
    elif c == "D0":
        k = 1.0
        cnt += b
    elif c == "F":
        k = 0.0
        cnt += b
    else:
        continue

    A += b * k  # 학점 * 과목평점의 총합

print(A / cnt)

