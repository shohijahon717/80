x = float(input('x = '))
y = float(input('y = '))

a = x
b = y

if x > y:
    y = (x+y)/2
    x = x*b*2
   
elif x == y:
    x = x
    y = y
else:
    x = (x+y)/2
    y = a*y*2

print(f"x = {x}")
print(f'y = {y}')


    