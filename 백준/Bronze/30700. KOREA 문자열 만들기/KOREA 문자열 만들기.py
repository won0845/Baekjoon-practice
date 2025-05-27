S = input()

target_list = ['K', 'O', 'R', 'E', 'A']

length = 0
index = 0

for s in S:

    if s == target_list[index]:
        length += 1
        index += 1
    
    if index == len('KOREA'):
        index = 0

print(length)