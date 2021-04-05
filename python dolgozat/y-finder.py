a = input("Te megadsz egy karaktersorozatot én megmondom van-É benne\n y-ra végződő kétjegyű mássalhangzó!: ")
f = ""
b = "ty"
c = "gy"
d = "ny"
e = "ly"
if a == "":
    print("Ez nem jó")
for cv in range(len(a)):
    if b in a:
     print(b)
     break
    elif c in a:
        print(c)
        break
    elif d in a:
        print(d)
        break
    elif e in a:
        print(e)
        break
    else:
        print("Nem jó")
        break
