import sys
input = sys.stdin.readline

N, M = map(int, input().split())

bucket = [i for i in range(1 , N+1)]

for _ in range(M):
    a , b = map(int, input().split())
    bucket[a-1], bucket[b-1] = bucket[b-1] , bucket[a-1]

print(' '.join(map(str, bucket)))
        
        