m = int(input("dati un numar: "))
n = int(input("dati puterea: "))
puterea = 0
adevarat = ''
m = 1
for m in range(1,n):
    puterea = m ** m
    if puterea == n:
        adevarat = 'DA'
    m += 1
if adevarat == 'DA':
    print("Da")
else:
    print("Nu")