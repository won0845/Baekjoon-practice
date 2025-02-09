s2s = {'miss':0, 'bad':200, 'cool':400, 'great':600, 'perfect':1000}
note, status = input().split()
print(int(note)*s2s[status])