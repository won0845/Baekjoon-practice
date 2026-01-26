def solution(bin1, bin2):
    answer = []
    
    a = bin1[::-1]
    b = bin2[::-1]
    
    carry = 0
    
    for i in range(max(len(a), len(b))):
        bit_a = int(a[i]) if i < len(a) else 0
        bit_b = int(b[i]) if i < len(b) else 0
        
        s = (bit_a + bit_b + carry)
        answer.append(str(s % 2))
        carry = s // 2
        
        
        
    if carry:
        answer.append('1')

    return ''.join(answer[::-1])
    
    
    return answer