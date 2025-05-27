n=int(input())

y, m=2024, 8
month=(n-1)*7
m+=month
if m%12==0:
  y+=(m//12)-1
  m=12
else:
  y+=(m//12)
  m%=12
print(y, m)