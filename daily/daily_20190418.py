x = [1, 2, 3]
y = []
prod = 1
for a in x:
    prod *= a
for a in x:
    y.append(prod/a)
print(x)
print(y)

x = [1, 2, 3]
y = []
i = 0
while i < len(x):
    z = x
    z = z[:i] + z[i+1:]
    prod = 1
    for a in z:
        prod *= a
    y.append(prod)
    i += 1
print(x)
print(y)
