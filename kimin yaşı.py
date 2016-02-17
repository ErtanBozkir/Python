aile=["ertan","halime","aysun","ercan"]
yas=[]
for i in aile:
    yas.append(int(input(i+" nın yaşını giriniz=>")))


girilen_yas=int(input("bir yaş giriniz"))

index=0
for i in yas:
    if girilen_yas>i:
        print(aile[index])
    index+=1
    