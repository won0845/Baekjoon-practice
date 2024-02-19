import sys
input = sys.stdin.readline

N = int(input())
count = 0

for _ in range(N):
    words = input()
    error = 0
    for i in range(len(words) - 1):
        if words[i] != words[i + 1]:
            new_word = words[i + 1:]
            if words[i] in new_word:
                error += 1
    if error == 0:
        count += 1
print(count)
