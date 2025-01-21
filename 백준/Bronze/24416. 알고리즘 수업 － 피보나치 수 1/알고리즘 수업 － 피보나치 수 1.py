
cnt2 = 0
fibo = {0:0, 1:1, 2:1}


    
def fibonacci(n):
    global cnt2
    
    for i in range(3, n+1):
        cnt2 += 1

        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n]

inp = int(input())

print(fibonacci(inp), cnt2)
