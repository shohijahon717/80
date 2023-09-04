n = int(input('n = '))

m = int(input('m = '))
k = n
a = 0
while k-m>=0:
    a+=1
    k-=m
print(f"Butun qismi: {a}, qoldiq: {k}")
    