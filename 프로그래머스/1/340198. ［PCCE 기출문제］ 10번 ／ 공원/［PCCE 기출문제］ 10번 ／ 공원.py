def solution(mats, park):
    # normalize park -> 2D list of strings
    grid = park
    
    R = len(grid)
    if R == 0:
        return -1
    C = len(grid[0])

    # mats 큰 것부터 검사
    for size in sorted(mats, reverse=True):
        if size > R or size > C:
            continue  # 공원보다 큰 매트는 불가능
        # 모든 가능한 top-left 위치 확인
        for r in range(R - size + 1):
            for c in range(C - size + 1):
                ok = True
                # SxS 내부가 모두 "-1"인지 검사
                for i in range(r, r + size):
                    for j in range(c, c + size):
                        if grid[i][j] != "-1":
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    return size
    return -1
