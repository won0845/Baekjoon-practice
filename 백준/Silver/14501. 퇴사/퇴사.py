n = int(input())
value =[]
dp = [0 for _ in range(n+1)]
for _ in range(n):
    a, b = map(int, input().split())
    value.append([a,b])

for i in range(n-1, -1, -1):
    # 마지막 날에는 상담을 아예 할 수가 없다.
    # 뒤에서 둘째 날 부터 비교
    if i+value[i][0] > n:
        # 시간이 부족해서 당일 상담을 못하는 경우 전에 기록을 사용(전날이 아닌 다음날)
        dp[i] = dp [i+1]
    else:
        # 시간이 되지만 안하는 경우와 하는경우 값을 비교하여 큰거 채택
        # 하는 경우 값 -> 현재 상담 값과 이 상담을 했을 경우 이전값을 더해서 산출
        # 이전 값 -> 상담에 걸리는 날짜 뒤에 값을 가져옴
        dp[i] = max(dp[i+1],value[i][1]+dp[value[i][0]+i])
        
print(dp[0])