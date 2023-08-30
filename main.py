import sqlite3
import time

print("""
************
Kütüphanem
************

""")

time.sleep(1)

print("""
lütfen yapmak istediğiniz işlemi seçiniz...

1 -------> Kütüphaneye yeni kitap kaydetmek istiyorum.
2 -------> Kitap aramak istiyorum.
3 -------> Prpgramı kapatmak istiyorum.
4--------> kütüphaneden bir kitap silmek istiyorum.


.""")

time.sleep(1)



time.sleep(1)

while True:
    a = int(input("Size yardımcı olabilmek için lütfen 1-3 arasındaki işlem komutlarından birisini giriniz"))
    if a == 3:
        print("Pekala... yardıma ihtiyacın olduğunda buralarda olacağım...")
        break
    elif a == 1:
        con = sqlite3.connect("kütüphane.db")
        cursor = con.cursor()
        cursor.execute("create table if not exists tablo('kitap_adı' text, 'yazar_ismi' text, 'tür' text, 'sayfa_sayısı' int)")
        con.commit()

        def kitap_ekle(kitapadı,yazaradı,tür,sayfasayısı):
            cursor.execute("insert into tablo values(?,?,?,?)" , (kitapadı,yazaradı,tür,sayfasayısı))
            con.commit()
        kitapadı = input("lütfen eklemek istediğiniz kitabın adını yazınız...")
        yazaradı= input("lütfen eklemek istediğiniz kitabın yazarını yazınız...")
        tür = input("lütfen eklemek istediğiniz kitabın türünü yazınız... öykü, roman, vb.")
        sayfasayısı = int(input("lütfen eklemek istediğiniz kitabın sayfa sayısını giriniz."))

        kitap_ekle(kitapadı,yazaradı,tür,sayfasayısı)
        print("kitabınız başarıyla eklendi... {} - {} - {}".format(kitapadı, yazaradı, tür))


    elif a == 2:
        b = input("lütfen ne ile arama yapmak istediğinizi belirtin\n"
                  "yazar adı, kitap adı ya da türe göre arama yapabilir ya da tüm kitaplarınızı listeleyebilirsiniz...")

        if b == "yazar adı" or b == "yazar":
            isim = input("lütfen aramak istediğiniz kitabın yazarını yazınız...")
            def yazarara(x):
                con = sqlite3.connect("kütüphane.db")
                cursor = con.cursor()
                cursor.execute("select * from tablo where yazar_ismi = '{}' ".format(x))
                liste1 = cursor.fetchall()
                for i in liste1:
                    print(i)
            yazarara(isim)


        elif b == "kitap adı" or b =="kitap":
            isim = input("lütfen aramak istediğiniz kitabın adını yazınız...")
            def kitapara(x):
                con = sqlite3.connect("kütüphane.db")
                cursor = con.cursor()
                cursor.execute("select * from tablo where kitap_adı= '{}' ".format(x))
                liste2 = cursor.fetchall()
                for i in liste2:
                    print(i)
            kitapara(isim)
        elif b== "tür":
            isim = input("lütfen aramak istediğiniz kitabın türünü yazınız...")
            def türara(x):
                con = sqlite3.connect("kütüphane.db")
                cursor = con.cursor()
                cursor.execute("select * from tablo where tür = '{}'". format(x))
                liste3 = cursor.fetchall()
                for i in liste3:
                    print(i)
            türara(isim)

        elif b == ("bütün kitaplar") or b == ("tüm kitaplar"):
            con = sqlite3.connect("kütüphane.db")
            cursor = con.cursor()
            cursor.execute("select * from tablo")
            liste4 = cursor.fetchall()
            for i in liste4:
                print(i)
        else:
            print("lütfen kitap adı, yazar adı ya da tür seçiniz.")





    else:
        print("Lütfen geçerli bir değer giriniz...")
    l = input("devame etmek istiyor musunuz?")
    if l == "hayır":
        break











