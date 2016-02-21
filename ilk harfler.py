gir=str(input("bir metin giriniz:"))
a=[gir]
for i in gir:
    if " "==i:
        b=gir.index(" ")
        print(b+1)
    if "."==i:
        b=gir.index(".")
        print(b+1)
print(gir.index(gir[0]))