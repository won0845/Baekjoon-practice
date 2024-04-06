import re
n = input()
print(sum(map(int, re.findall("\d+", input().rstrip()))))
