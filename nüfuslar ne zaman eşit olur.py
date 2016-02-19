a_nüfus=int(input("A şehrinin nüfusunu giriniz:"))
b_nüfus=int(input("B şehrinin nüfusunu giriniz:"))
say=0
while True:
    if a_nüfus>=b_nüfus:
        break

    a_nüfus=a_nüfus*125/100
    b_nüfus=b_nüfus*112/100
    say=say+1
print(say,"Yıl sonra A ve B şehrinin Nüfusları Eşit olur.")