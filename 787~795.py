# 787

a = []
for n in range(6):
    a.append(input('Element? ' ))

b = []

for i in range(0, 6, 2):
    b.append(a[i])

for j in range(1, 6, 2):
    b.append(a[j])

print(b)

# 788

num = []
for _ in range(1, 16):
    num.append(_)

a = int(input())
b = []

for n in num:
    if n % a == 0:
        b.append(n)

print(b)

# 790

a = []
for i in range(-1, -6, -1):
    a.append(i)

print(a)

# 791

a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = []

for i in range(a[1]):
    c.append(a[0])

for j in range(b[1]):
    c.append(b[0])

print(c)

# 792

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

# 793

a = list(map(str, input()))

a.reverse()

print(a)

# 795

a = list(map(str, input().split()))

a.reverse()

print(a[1:len(a)-1])