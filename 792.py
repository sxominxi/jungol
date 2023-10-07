a = []

for n in range(4):
    a.extend(input("Input? " ).split())

b = []
c = []
for i in range(8):
    if i % 2 == 0:
        b.append(a[i])
    else:
        c.append(a[i])

print(f'Color: {b}')
print(f'Animal: {c}')