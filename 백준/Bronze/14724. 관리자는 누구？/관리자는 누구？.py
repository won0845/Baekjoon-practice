N = int(input())
dict = {}
circle = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']

for i in range(9):
  member = list(map(int, input().split()))
  dict[circle[i]] = max(member)

high = list(dict.values())	# dict에서 value값만 빼와서 리스트로 만들기
max_high = high.index(max(high))	# 위의 high에서 가장 큰 값의 인덱스 뽑기
print(circle[max_high])	# 인덱스에 해당하는 동아리명 print