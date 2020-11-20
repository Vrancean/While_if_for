x = int(input("dati prima latura: "))
y = int(input("dati a doua latura: "))
z = int(input("dati a treia latura: "))
if (x + y > z) and (x + z > y) and (y + z > x):
    if ((x == y) and (x != z)) or ((x == z) and (x != z)) or ((y == z) and (y != x)):
        print("este un tringhi isoscel")
    elif (x == y) and (x == z):
        print("este un triunghi echilateral")
    else:
        print("este un triunghi scalen")
else:
    print("nu este un tringhi")