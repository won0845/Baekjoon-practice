def solution(id_pw, db):
    answer = ''
    member = {}
    
    for id, pw in db:
        member[id] = pw
        
    w_id = id_pw[0]
    w_pw = id_pw[1]
    
    if member.get(w_id) == w_pw:
        return "login"
    elif member.get(w_id) == None:
        return "fail"
    else :
        return "wrong pw"