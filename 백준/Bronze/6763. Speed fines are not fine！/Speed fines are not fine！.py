limit = int(input())
ob = int(input())

aboveSpeend = ob - limit

if 1<= aboveSpeend <= 20:
    print("You are speeding and your fine is $100.")
elif 21 <= aboveSpeend <= 30:
    print("You are speeding and your fine is $270.")
elif 31 <= aboveSpeend:
    print("You are speeding and your fine is $500.")
else:
    print("Congratulations, you are within the speed limit!")