ailesayısı=int(input("aile sayısı giriniz"))
aile=[]
yas=[]
sayi=0
while True:

    if ailesayısı==sayi:
        break
    else:
        aile.append(input(" ailenin"+ " "+ str(sayi+1)+"." +" elemanını giriniz"))
        yas.append(input("ailenin"+ " "+ str(sayi+1)+"."+ " " +"elemanının yaşını giriniz"))
    sayi=1+sayi

istenilen=(input("kimin yaşını istiyorsunuz"))

for i in aile:
    if istenilen==i:
        istenilenindex=aile.index(istenilen)
        print(yas[istenilenindex])
