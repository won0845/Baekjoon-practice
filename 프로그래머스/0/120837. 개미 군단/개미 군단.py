def solution(hp):
    
    generals = hp // 5
    hp %= 5

    soldiers = hp // 3
    hp %= 3

    workers = hp  
    
    answer = generals + soldiers + workers
    return answer