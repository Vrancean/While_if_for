x = int(input("Dati virsta lui Mihai, mai mica de 20: "))
s= 1
s2= 0
y= 0
if x<20:
    for x in range (1, x + 1):
        s=s*2 + x
    print("La", x,"ani primeste", s,"$")
    while s2 <= 100:
        y+= 1
        s2=s2*2+y
    print("Mihai primeste 100 de dolari la", y,"ani")
else:
    print("Mai mare de 20 ani")