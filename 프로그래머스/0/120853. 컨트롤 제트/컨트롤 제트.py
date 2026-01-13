def solution(s):
    k = s.split(" ")
    print(k)
    keep = ""
    hap = 0
    for i in k:
        if i == "Z":
            hap -= int(keep)
        else:
            hap += int(i)
            keep = i
    answer = hap
    return answer