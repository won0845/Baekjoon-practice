n = int(input())

count = 0
new = n
while True:
    
    a = new // 10
    b = new % 10
    c = a + b
    new = b * 10 + c % 10
    count += 1
    if new == n:
        break

print(count)
