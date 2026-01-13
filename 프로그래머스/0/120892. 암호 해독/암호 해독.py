def solution(cipher, code):
    answer = []
    leg = code
    while leg <= len(cipher):
        answer.append(cipher[leg-1])
        leg += code
    return "".join(answer)