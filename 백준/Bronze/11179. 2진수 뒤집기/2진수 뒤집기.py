n = int(input())

binary = []
answer = 0

while n > 0:
    mob = n % 2
    n //= 2
    binary.append(mob)


for i in range(len(binary)):
      answer += binary[i] * (2 ** (len(binary) - 1 - i))

print(answer)
