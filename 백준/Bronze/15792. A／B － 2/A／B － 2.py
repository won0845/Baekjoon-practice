a, b = map(int, input().split())
print(a // b, end = '') # 우선 몫을 출력

if a % b: # 나머지가 있다면
    print('.', end='') # 점(.)을 출력해주고
    i = 0
    
    while a % b and i < 1000: 
        a = a % b * 10 # 계속 10씩 곱해주면서 몫을 뒤에 붙여줌 
        i += 1
        print(a // b, end = '')