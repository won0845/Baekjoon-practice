	# 수열n 쿼리q
n,q = map(int,input().split())
 
# 길이 n의 수열
board = list(map(int,input().split()))
 
for qq in range(q):
 
    # 쿼리
    query = list(map(int,input().split()))
 
    # 1번 쿼리이면
    if query[0] == 1:
 
        # a,b 구간의 합
        print(sum(board[query[1]-1:query[2]]))
 
        # 스왑
        board[query[1]-1], board[query[2]-1] = board[query[2]-1], board[query[1]-1]
    else:
 
        # a,b구간의 합 - c,d구간의 합
        print(sum(board[query[1]-1:query[2]])-sum(board[query[3]-1:query[4]]))