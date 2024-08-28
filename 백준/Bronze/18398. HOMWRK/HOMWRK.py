n = int(input())
for i in range(n):
    problems = int(input())
    for j in range(problems):
        numbers = list(map(int, input().split()))
        print(numbers[0] + numbers[1], numbers[0] * numbers[1])
