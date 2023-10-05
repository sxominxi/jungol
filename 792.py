a = []
for i in range(4):
    x = input().split()
    y, z = *x
    a.append(y)
    a.append(z)

print(a)

b = []
c = []

for j in range(8):
    if j % 2 == 0:
        b.append(a[j])
    else:
        c.append(a[j])

print(f'Color : {b}') 
print(f'Animal : {c}') 