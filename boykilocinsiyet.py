boy=float(input("boyunuzu giriniz(M):"))
kilo=float(input("kilonuzu giriniz(KG):"))
cinsiyet=input("cinsiyetinizi giriniz:")
endex= kilo/(boy*boy)
if endex<18.5:
    print("zayıf")
elif endex<25:
    print("Normal")
elif endex<30:
    print("fazla kilolu")
elif endex<35:
    print("şişman(obez)-1.Sınıf")
elif endex<45:
    print("şişman(obez)-2.sınıf")
elif endex>45:
    print("öldün çık")
