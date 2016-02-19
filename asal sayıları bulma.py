"""gir=int(input("bir sayı giriniz:"))
listet=[]
while True:
    if gir==1:
        break
    for a in range(2,gir-1):
        if gir%a!=0:
            listet.append(gir)
    gir=gir-1
print(listet)
"""
listet=[]
tut=True
gir=int(input("bir sayı giriniz:"))
while True:
    if gir==1:
        break
    for a in range(2,gir):
        if gir%a==0:
            tut=False
            break
    if tut:
        listet.append(gir)
    else:
        tut=True
    gir=gir-1
print(listet)



"""gir=int(input("bir sayı giriniz:"))
liste=[]
for i in range(2,gir-1):
    if gir%i==1:
        liste.append(gir)
print(liste)"""