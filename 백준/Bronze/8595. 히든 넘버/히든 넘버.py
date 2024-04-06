import re
n = int(input())
number = "1234567890"
print(sum(map(int, re.findall("\d+", input().rstrip()))))
