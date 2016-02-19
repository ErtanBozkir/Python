gir=int(input("bir sayı giriniz:"))
toplam=1
while True:
    if gir==1:
        break
    else:
        toplam=toplam*gir
        gir=gir-1
print(toplam)