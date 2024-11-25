STR, DEX, INT, LUK, N = map(int, input().split())

total_status = STR + DEX + INT + LUK

if total_status < (4 * N):
    print((4 * N) - total_status)
else:
    print(0)