n = int(input())
lst = list(map(int, input().split()))

jun = len(lst)
chan = lst.count(1)  
ban = lst.count(-1)
gi = jun-chan-ban

if jun / 2 <= gi:
    print("INVALID")
elif chan > ban:
    print("APPROVED")
elif chan <=ban:
    print("REJECTED")


