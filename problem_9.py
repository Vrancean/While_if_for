x = int(input("Dati un numar: "))
s = 0
if (x != 0) and (x != 1):
    for i in range (1, x):
        if x % i == 0:
            s += i
    if s == x:
        print("Numarul", x,"este perfect")
    else:
        print("Numarul", x,"nu este perfect")