stamp = int(input())
price = int(input())

discount = 0 

if stamp >= 20:
    discount = max(price // 4, 2000)
elif stamp >= 15:
    discount = max(2000, price // 10)
elif stamp >= 10:
    discount = max(price // 10, 500)
elif stamp >= 5:
    discount = 500
else:
    discount = 0

finals = max(0, price - discount)
print(finals)