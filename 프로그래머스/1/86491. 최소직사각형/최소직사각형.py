def solution(sizes):
    max_w = 0
    max_h = 0

    for w, h in sizes:
        w, h = max(w, h), min(w, h)  # 회전해서 큰 변을 w로 통일
        max_w = max(max_w, w)
        max_h = max(max_h, h)

    return max_w * max_h
