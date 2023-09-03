d = int(input('day: '))
m = int(input('month: '))
  
if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    if 1<=d<=30:
        d=d+1
        print(f"{d}.{m}")
    elif d == 31 and 1<=m<=11:
        d = 1
        m = m + 1
        print(f"{d}.{m}")
    elif d == 31 and m == 12:
        d = 1 
        m = 1
        print(f"{d}.{m}")
    else:
        print("Bunday sana yo'q!")
elif m == 4 or m == 6 or m == 9 or m == 11:
    if 1<=d<=29:
        d=d+1
        print(f"{d}.{m}")
    elif d == 30 and 1<=m<=11:
        d = 1
        m = m + 1
        print(f"{d}.{m}")
    elif d == 30 and m == 12:
        d = 1 
        m = 1
        print(f"{d}.{m}")
    else:
        print("Bunday sana yo'q!")
elif m == 2:
    if 1<=d<=27:
        d = d + 1
        print(f"{d}.{m}")
    elif d == 28:
        d = 1
        m = m + 1
        print(f"{d}.{m}")
    else:
        print("Bunday sana yo'q!")
else:
    print("Bunday sana yo'q!")
    

        