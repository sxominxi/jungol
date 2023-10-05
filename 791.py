a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = []

for i in range(a[1]):
    c.append(a[0])

for j in range(b[1]):
    c.append(b[0])

print(c)