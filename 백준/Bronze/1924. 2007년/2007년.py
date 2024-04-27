
m, d = map(int, input().split())
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum1 = 0

for i in range(m-1):
    sum1 += (month[i])
daye = (sum1 + d) % 7

print(day[daye])
