x=int(input("introdu x: "))
s=0
for i in range(1,x+1):
    p=1
    for x in range(1,i+1):
        p*=x
    s+=p
    print("",s)