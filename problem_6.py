v = int(input("dati un numar :"))
s1 = 0
s2 = 0
for x in range (1, v + 1):
    s1 += x ** 3
for x in range (1, v + 1):
    s2 += x
s2 = s2 ** 2
print("s1 = ", s1)
print("s2 = ", s2)
if s1 > s2:
    print("s1 > s2")
elif s2 > s1:
    print("s2 > s1")
else:
    print("s1 = s2")

v = int(input("dati un numar:"))
s1 = 0
s2 = 0
for y in range (1, v + 1):
    s1 += y ** 2
s1 = 3 * s1
print("s1 = ", s1)
for y in range (1, v + 1):
    s2 += y
s2 = v ** 3 + v ** 2 + s2
print("s2 = ", s2)
if s1 > s2:
    print("s1 > s2")
elif s2 > s1:
    print("s2 > s1")
else:
    print("s1 = s2")
