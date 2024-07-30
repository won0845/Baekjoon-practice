string = input()

for i in string:
    if i.isupper():
        print(i.lower(),end="")
    else:
        print(i.upper(),end="")