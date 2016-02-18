gir=int(input("bir sayı giriniz:"))
liste=[]
a=0
while True:
    if gir==a:
        break
    else:
        liste.append(int((gir)))
    gir=gir-1
print((sum(liste)))

"""
gir=int(input("bir sayı giriniz:"))
toplam=0
while True:
    if gir==0:
        break
    else:
        toplam=toplam+gir

    gir=gir-1

print(toplam)
"""