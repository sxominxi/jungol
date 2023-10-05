num = []
for _ in range(1, 16):
    num.append(_)

a = int(input())
b = []

for n in num:
    if n % a == 0:
        b.append(n)

print(b)