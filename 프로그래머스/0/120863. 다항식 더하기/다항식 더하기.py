def solution(polynomial):
    new = polynomial.replace(" ", "").split("+")
    
    x_sum = 0
    c_sum = 0

    for i in new:
        if "x" in i:
            coef = i.replace("x","")
            x_sum += int(coef) if coef else 1
        else:
            c_sum += int(i)
            
    parts = []
    if x_sum:
        parts.append("x" if x_sum == 1 else f"{x_sum}x")
    if c_sum:
        parts.append(str(c_sum))
    
    answer = " + ".join(parts)
    return answer