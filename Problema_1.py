x=int(input('dati numarul de zile: '))
if x==28 or x==29:
    print("Luna: ",'februarie') 
elif x==30:
    print("Lunile: ",'iunie','aprilie','septembrie','noiembrie')   
elif x==31:
    print("Lunile: ",'decembrie','martie','iulie','mai','august','octombrie','ianuarie') 
elif x<28 or x>31:
    print('Nu exista luna cu asa numar de zile')