n = int(input())

for i in range(n):
    cost, pay = map(float, input().split())
    change = pay - cost
    fifty = int(change)// 50
    change = change-(fifty * 50)
    twenty = int(change) // 20
    change = change-(twenty * 20)
    ten = int(change) // 10
    change = change-(ten*10)
    five = int(change) // 5
    change = change-(five*5)
    one = int(change)
    print(f"{fifty}-$50, {twenty}-$20, {ten}-$10, {five}-$5, {one}-$1")
    