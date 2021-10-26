Troom, Tcond = map(int, input().split())
R = input()
Y = Troom
if R == "freeze":
    Y = min(Troom, Tcond)
if R == "heat":
    Y = max(Troom, Tcond)
if R == "auto":
    Y = Tcond
print(Y)
