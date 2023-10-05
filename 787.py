a = []
for n in range(6):
    a.append(input('Element? ' ))

b = []

for i in range(0, 6, 2):
    b.append(a[i])

for j in range(1, 6, 2):
    b.append(a[j])

print(b)