kactane=int(input("kaç tane sayı girmek istiyorsunuz:"))
sayilar=[]
while True:
    if kactane==0:
        break
    else:
        sayilar.append(int(input(str(kactane) + ". sayıyı giriniz:")))
        kactane=kactane-1


"""print(sayilar)"""
for a in range(0,len(sayilar)):
    for i in range(a+1,len(sayilar)):
         if ((i+1)!=len(sayilar)) and (sayilar[a]<sayilar[(i)]):
            c=sayilar[a]
            sayilar[a]=sayilar[i]
            sayilar[i]=c



print(sayilar)



"""sayilar.sort(reverse=True)
print(sayilar)

"""

