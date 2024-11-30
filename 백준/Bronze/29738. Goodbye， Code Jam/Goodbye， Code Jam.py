n = int(input())

for i in range(n):
    a = int(input())
    print(f"Case #{i+1}:",end=" ")
    if a <= 25:
        print("World Finals")
    elif a <= 1000:
        print("Round 3")
    elif a <= 4500:
        print("Round 2")
    else:
        print("Round 1")
   