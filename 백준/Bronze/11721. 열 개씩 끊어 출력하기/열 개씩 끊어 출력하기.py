string = input().strip()

while len(string) > 0:
    print(string[:10])
    string = string[10:]