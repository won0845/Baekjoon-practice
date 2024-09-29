n = int(input())  # 주어진 n 값 입력
code = input()    # 암호화된 문자열 입력

for i in range(0, len(code), n):
    print(code[i], end="")