Aa, Al = map(int, input().split())
Ba, Bl = map(int, input().split())

As = Al
Bs = Bl
while As > 0 and Bs > 0:
    As -= Ba
    Bs -= Aa

if As <= 0 and Bs <=0:
    print("DRAW")
elif As <= 0 and Bs > 0:
    print("PLAYER B")
elif As > 0 and Bs <=0:
    print("PLAYER A")