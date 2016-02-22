import sqlite3
vt=sqlite3.connect('C:/Users/lenovo/Desktop/python/bankadatabase.sqlite')
cur=vt.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS hesaplar (isim,soyisim,sifre,tc,bakiye)")
while True:
    giris=int(input("giriş yapmak için 1'i\nüye olmak için 2'yi tıklayınız:\nçıkmak için 3'ü tıklayınız:"))
    if giris==1:
        giristc=int(input("tc giriniz:"))
        girissifre=int(input("şifre giriniz:"))
        cur.execute("""SELECT * FROM hesaplar WHERE sifre = '%s' AND tc = '%s'"""%(girissifre, giristc))
        loginSonucu=cur.fetchall()

        if len(loginSonucu)==0:
            print("uye yok")
        elif len(loginSonucu)!=0:
            girisyapti=int(input("\nPara yatırmak için 1'i\nPara çekmek için 2'yi\nBakiye sorgulamak için 3'ü\nBorç ödemek için 4'ü\nAna menüye dönmek için 5'ü tıklayınız:"))
            if girisyapti==1:
                parayatirma=int(input("\nkendi hesabınıza para yatırmak için 1'e\nBaşka hesaba para yatırmak için 2'ye\nmenüye dönmek için 3'e tıklayınız:"))
                if parayatirma==1:
                    cur.execute("""SELECT bakiye FROM hesaplar WHERE tc= '%d'"""%(giristc))
                    bakiyesonuc=cur.fetchone()
                    kendihspytrilan=int(input("\nyatırmak istediğiniz tutarı giriniz:"))
                    guncelbakiye=int(bakiyesonuc[0])+kendihspytrilan
                    cur.execute("""UPDATE hesaplar SET bakiye = '%d' WHERE tc='%d'"""%(guncelbakiye,giristc))
                    vt.commit()
                    #cur.execute("UPDATE hesaplar SET bakiye='10' WHERE tc=789456")
                    cur.execute("""SELECT bakiye FROM hesaplar WHERE tc= '%d'"""%(giristc))
                    bakiyesonuc=cur.fetchall()
                    print("Güncel bakiyeniz:",bakiyesonuc)
                if parayatirma==2:
                    cur.execute("""SELECT bakiye FROM hesaplar WHERE tc='%d'"""%(giristc))
                    kendibakiyesi=cur.fetchone()
                    baskatc=int(input("\nPara yatırmak istediğiniz kişinin tc'sini giriniz:"))
                    cur.execute("""SELECT bakiye FROM hesaplar WHERE tc='%d'"""%(baskatc))
                    baskatcbakiyesi=cur.fetchone()
                    yatirilanmiktar=int(input("Yatırmak istediğiniz miktarı giriniz:"))
                    kendibakiyesi=int(kendibakiyesi[0])-yatirilanmiktar
                    cur.execute("""UPDATE hesaplar SET bakiye='%d' WHERE tc='%d'"""%(kendibakiyesi,giristc))
                    baskatcyatirilan=yatirilanmiktar+int(baskatcbakiyesi[0])
                    cur.execute("""UPDATE hesaplar SET bakiye  ='%d' WHERE tc='%d'"""%(baskatcyatirilan,baskatc))

                if parayatirma==3:
                    print("Menüye yönlendiriliyorsunuz...")


            if girisyapti==2:
                cur.execute("""SELECT bakiye FROM hesaplar WHERE tc= '%d'"""%(giristc))
                bakiyesonuc2=cur.fetchone()
                cekilenpara=int(input("Çekmek istediğiniz miktarı giriniz:"))
                guncelbakiye2=int(bakiyesonuc2[0])-cekilenpara
                cur.execute("""UPDATE hesaplar SET bakiye ='%d'"""%(guncelbakiye2))
                vt.commit()
                cur.execute("""SELECT bakiye FROM hesaplar WHERE tc= '%d'"""%(giristc))
                bakiyesonuc5=cur.fetchone()
                print("güncel bakiyeniz:",bakiyesonuc5[0])
            if girisyapti==3:
                cur.execute("""SELECT  bakiye FROM hesaplar WHERE tc='%d'"""%(giristc))
                bakiyesorgu=cur.fetchone()
                print("bakiyeniz:",bakiyesorgu)
            if girisyapti==4:
                cur.execute("""SELECT bakiye FROM hesaplar WHERE tc='%d'"""%(giristc))
                borcvarmi=cur.fetchone()
                if int(borcvarmi[0])<0:
                    print("toplam borcunuz:",borcvarmi[0])
                    nekadaröde=int(input("ödemek istediğiniz miktarı giriniz:"))
                    guncelbakiye3=int(borcvarmi[0])+nekadaröde
                    cur.execute("""UPDATE hesaplar SET bakiye='%d'"""%(guncelbakiye3))
                    vt.commit()
                    cur.execute("""SELECT bakiye FROM hesaplar WHERE tc='%d'"""%(giristc))
                    bakiyesorgu3=cur.fetchone()
                    print("Bakiyeniz:",bakiyesorgu3)
                if int(borcvarmi[0])>=0:
                    print("Borcunuz bulunmamaktadır.")
            if girisyapti==5:
                print("Ana menüye yönlendiriliyorsunuz...")



    elif giris==2:
        isim=input("isminizi giriniz:")
        soyisim=input("soyisminizi giriniz:")
        tc=int(input("tc giriniz:"))
        cur.execute("""SELECT tc FROM hesaplar WHERE tc= '%d'"""%(tc))
        zatenvar=cur.fetchall()
        sifre=(input("şifrenizi giriniz:"))
        cur.execute("""INSERT INTO hesaplar VALUES ('%s', '%s','%s','%d',0)"""%(isim, soyisim,sifre,tc))
        vt.commit()
    elif giris==3:
        break


