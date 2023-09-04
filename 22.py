def IsPrime(N):
    a = 0
    for i in range(2, N):
        if N % i == 0:
            a += 1
    if a == 0:
        return True
    else:
        return False

k = int(input("k = "))

b = 0
for i in range(1,k+1):
    son = int(input(f'{i}-son: '))
    if IsPrime(son) == True:
        b += 1

print(b)