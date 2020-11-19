from fractions import Fraction
n1 = int(input("dati numaratorul:"))
m1 = int(input("dati numitorul:"))
n2 = int(input("dati numaratorul:"))
m2 = int(input("dati numitorul:"))
adunarea = (Fraction(n1,m1)+Fraction(n2,m2))
inmultirea = (Fraction(n1,m1)*Fraction(n2,m2))
print("adunarea =",adunarea)
print("înmulțirea =",inmultirea)
