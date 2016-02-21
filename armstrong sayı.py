sayi=int(input("bir sayı giriniz:"))
a=str(sayi)
liste=[]
for i in range(0,len(a)):
    liste.append(int(a[i])**len(a))
if sum(liste)==int(sayi):
    print(a + " armstrong sayıdır")
else:
    print(a + " armstrong sayı değildir")