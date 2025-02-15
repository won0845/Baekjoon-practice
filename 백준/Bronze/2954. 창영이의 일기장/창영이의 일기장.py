#  반복문 돌려서 aeiou중에 있다면 -> 맨처음꺼 저장 후 3칸 뛰고 다음으로 넘어감 
n = input()
i = 0
mo = ["a", "e", "i", "o", "u"]
ans = []
while i < len(n):
    ans.append(n[i])
    if n[i] in mo:
        i+=3
    else:
        i+=1
print("".join(ans))
        