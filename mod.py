gir=int(input("bir sayı giriniz:"))

toplam=0
while True:
    if gir<1:
        break
    else:
        toplam=toplam+gir%10
        gir=int(gir/10)
print(toplam)