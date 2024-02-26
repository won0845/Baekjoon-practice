import sys

input = sys.stdin.readline

n = int(input())
Llist = list(map(int, input().split()))

# 좌표 압축 로직
Lset = sorted(set(Llist))  # 중복 제거 후 정렬
# 각 좌표에 대한 압축된 값의 인덱스를 저장하는 딕셔너리 생성
Ldict = {Lset[i]: i for i in range(len(Lset))}

# 압축된 값의 인덱스 출력
for i in Llist:
    print(Ldict[i], end=' ')
