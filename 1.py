a = float(input('a = '))
b = float(input("b = "))
c = float(input('c = '))

if a >= b:
    if b >= c:
        print(c)
    if b < c:
        print(b)
elif b > a:
    if a >= c:
        print(c)
    if a < c:
        print(a)
    