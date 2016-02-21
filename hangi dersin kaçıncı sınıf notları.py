
kactane=int(input("kaç tane öğrenci gireceksin:"))
ad=[]
soyad=[]
numara=[]
ders=[]
sınıf=[]
nott=[]
while True:
    if kactane==0:
        break
    else:
        ad.append(input("adı:"))
        soyad.append(input("soyadı:"))
        numara.append(int(input("numarası:")))
        sınıf.append((int(input("sınıfı:"))))
        ders.append((input("dersin adı:")))
        nott.append(int(input("notu:")))
        kactane=kactane-1
hangiders=input("hangi dersin notlarını istiyorsunuz:")
hangisınıf=int(input("kaçıncı sınıfın notlarını istiyorsunuz:"))
xd=[]

for i in range(0,len(ad)):
    if hangiders==ders[i] and hangisınıf==sınıf[i]:
        print(ad[i]," in ",ders[i]," notu ",nott[i])


