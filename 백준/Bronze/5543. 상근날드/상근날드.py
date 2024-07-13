ham = []
um = []
for i in range(3):
    ham.append(int(input()))
for i in range(2):
    um.append(int(input()))
  
ham.sort()
um.sort()
print(ham[0]+um[0]-50)