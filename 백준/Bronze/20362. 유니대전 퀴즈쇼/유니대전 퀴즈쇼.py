
import sys

N, S = sys.stdin.readline().rstrip().split()

write_mode = True
answer_list = []
answer = ''

for _ in range(int(N)):
    nickname, chat = sys.stdin.readline().rstrip().split()

    if write_mode and nickname != S:
        answer_list.append(chat)
    elif nickname == S:
        answer = chat
        write_mode = False

print(answer_list.count(answer))