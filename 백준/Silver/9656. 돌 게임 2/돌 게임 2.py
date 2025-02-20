n = int(input())
mob = 0
mod = 0

mob = n // 3
mod = n % 3
if (mob + mod) % 2 == 0:
    print("SK")
else:
    print("CY")
