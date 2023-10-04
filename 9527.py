a = list(map(str, input().split()))

for i in range(1, len(a)):
    a[i] = int(a[i])

print(f'name  kor  eng  mat  sum    avg')
print(f'     {a[0]}  {a[1]}    {a[2]}   {a[3]}  {a[1]+a[2]+a[3]} {(a[1]+a[2]+a[3])/3:.2f}')