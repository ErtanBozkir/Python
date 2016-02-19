kactane=int(input("kaç tane sayı girmek istiyorsunuz:"))

sayilar=[]
while True:
    if kactane==0:
        break
    else:
        sayilar.append(int(input(str(kactane) + ". sayıyı giriniz")))
        kactane=kactane-1
max=sayilar[0]
saydir=0
a=0

while saydir<len(sayilar):
    saydir=saydir+1
    if max<sayilar[a]:
        max=sayilar[a]
    a=a+1



print(max)





"""kactane=int(input("kaç tane sayı girmek istiyorsunuz:"))
sayilar=[]
while True:
    if kactane==0:
        break
    else:
        sayilar.append(int(input(str(kactane) + ". sayıyı giriniz")))
        kactane=kactane-1


print(max(sayilar))
"""