n = int(input())

binary = []
answer = 0

# 2진수로 변환
while n > 0:
    remainder = n % 2
    n //= 2
    binary.append(remainder)

# 2진수 뒤집어서 10진수로 변환
for i in range(len(binary)):
    answer += binary[i] * (2 ** (len(binary) - 1 - i))

print(answer)
