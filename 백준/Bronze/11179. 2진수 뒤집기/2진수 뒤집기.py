n = int(input())

binary = []
answer = 0

while n > 0:
    mob = n % 2
    n //= 2
    binary.append(mob)

binary.reverse()

for i in range(len(binary)):
     answer += binary[i] * (2 ** i)

print(answer)
