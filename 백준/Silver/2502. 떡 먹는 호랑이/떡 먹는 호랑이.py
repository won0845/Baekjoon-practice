day, dduk = map(int, input().split())

dp = [[1,0],[0,1]]

for i in range(2,day):
    dp.append([dp[i-2][0]+dp[i-1][0],dp[i-2][1]+dp[i-1][1]])

x, y = dp[day-1][0],dp[day-1][1]

a = 0 
b = 0;
b = int(dduk / y)
def cir(b):
    for i in range(b,0,-1):
        for j in range(1,int(dduk/x)):
            if x*j+y*i > dduk:
                break
            if (x*j+y*i) == dduk:
                print(j)
                print(i)
                return
cir(b)
        
    

