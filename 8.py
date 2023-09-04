s = float(input('summa: '))
f = float(input('foiz: '))

i = s
k = 0
while i <= 2*s:
    k += 1
    i = i*(1 +f/100)
    
print(k, i)