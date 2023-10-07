a = list(map(int, input().split()))

for n in a:
    if n % 3 != 0:
        a.remove(n)

print(a)