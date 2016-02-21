def kok(a,b,c):
    delta=((b*b)-(4*a*c))
    if (delta<0):
        print("denklemin gerçel (reel) kökü yoktur.")
        return
    x1=(((-1)*(b))-(delta**0.5))/(2*a)
    x2=((((-1)*b))+(delta**0.5))/(2*a)
    return(x1,x2)
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
sonuc=kok(a,b,c)
print(sonuc)

