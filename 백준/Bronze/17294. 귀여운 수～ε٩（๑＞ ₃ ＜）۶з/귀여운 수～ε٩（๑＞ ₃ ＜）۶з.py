s = input()
if len(s) <= 2:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    ok = 1
    t = int(s[0])-int(s[1])
    for i in range(1, len(s)-1):
        if int(s[i])-int(s[i+1]) != t:
            ok = 0
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!" if ok else "흥칫뿡!! <(￣ ﹌ ￣)>")