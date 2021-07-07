import time
import sqlite3

class sistem():

    def __init__(self,sistem_türü,komutanlık,sistem_ismi,envanter_giriş,miktar,durum):

        self.sistem_türü = sistem_türü
        self.komutanlık = komutanlık
        self.sistem_ismi = sistem_ismi
        self.envanter_giriş = envanter_giriş
        self.miktar = miktar
        self.durum = durum

    def __str__(self):

        return "Sistem Türü: {}\n Bağlı Olduğu Komutanlık: {}\n Sistem İsmi: {}\n Envanter Sayısı: {}\n Envanter Durumu: {}\n".format(self.sistem_türü,self.komutanlık,self.sistem_ismi,self.envanter_giriş,self.miktar,self.durum)


class envanter():

    def __init__(self):

        self.veritabanı_baglantı()



    def veritabanı_baglantı(self):

        self.veritabanı = sqlite3.connect("Askeri Envanter Veritabanı.db")
        self.cursor = self.veritabanı.cursor()

        self.cursor.execute("Create Table If Not Exists Envanter(Sistem_Türü TEXT,Komutanlık TEXT, Sistem_İsmi TEXT, Envanter_Giriş TEXT, Miktar INT, Durum TEXT)")
        self.veritabanı.commit()

        print("***** Askeri Envanter Veritabanı İçerisine Tablo Oluşturuldu *****")
        print("\n")


    def veritabanı_baglantı_kesme(self):

        self.veritabanı.close()



    def envanter_göster(self):

        self.cursor.execute("Select * from Envanter")
        envanterlistesi = self.cursor.fetchall()

        if (len(envanterlistesi) == 0):
            print("Envanterde Sistem Bulunmuyor.")

        else:
            for i in envanterlistesi:

                Envanterbilgisi = sistem(i[0],i[1],i[2],i[3],i[4],i[5])
                print(Envanterbilgisi)



    def envanter_bilgi_ekleme(self,sistem_türü,komutanlık,sistem_ismi,envanter_giriş,miktar,durum):

        self.cursor.execute("Insert Into Envanter Values(?,?,?,?,?,?)",(sistem_türü,komutanlık,sistem_ismi,envanter_giriş,miktar,durum))
        self.veritabanı.commit()

        print("***** Askeri Envanter Veritabanına Veri Eklendi *****")
        print("\n")






    def envanter_sorgulama(self,sistem_ismi):

        self.cursor.execute("Select * from Envanter where Sistem_İsmi = ?",(sistem_ismi,))
        Sistemliste = self.cursor.fetchall()

        if (len(Sistemliste) == 0):
            print("Envanterde Sistem Bulunmuyor.")

        else:
            for i in Sistemliste:
                Sistembilgisi = sistem(Sistemliste[0][0], Sistemliste[0][1], Sistemliste[0][2], Sistemliste[0][3], Sistemliste[0][4],Sistemliste[0][5])
                print(Sistembilgisi)


    def envanter_güncelleme(self,d1,d2,d3,d4):

        self.cursor.execute("Select * from Envanter where ? = ? ")
        liste = self.cursor.fetchall()
        print("Envanter Bilgisi Aktarılıyor...")
        time.sleep(1)
        print("\n")
        for i in liste:
            print(i)
            print("***********************")


        self.cursor.execute("Update Envanter set ? = ? where ? = ?",(d1,d2,d3,d4))
        self.veritabanı.commit()

        print("***** Envanter Güncellenmesi Tamamlandı *****")






# *************************************************************************************************************************

AEYS = envanter()




print("""*******************************************


Askeri Envanter Yönetim Programına Hoşgeldiniz !



*******************************************""")

print("\n")
time.sleep(1)





while True:

    print("********** Sisteme Giriş Yapabilmek İçin Lütfen Askeri ID Numaranızı Ve İsminizi Giriniz **********")

    ıd = int(input("Lütfen ID Numarasını Giriniz:"))
    name = input("Lütfen İsminizi Giriniz:")
    print("\n")




    if (ıd == 50803120380 and type(name) == str):

        print("***** Sisteme Güvenli Bir Şekilde Giriş Yapıldı *****")
        print("\n")
        print(""" ***************************************************
            
            Lütfen Sistem İçerisinde Yapmak İstediğiniz İşlemi Seçiniz ! 
            
            Envanteri Görüntülemek İçin: 1
            
            Envantere Yeni Veri Girmek İçin: 2
            
            Envanter İçerisinden Detaylı Bilgi Almak İçin: 3
            
            Envanter Veritabanını Güncellemek İçin: 4
            
            Envanter Veritabanı İçerisinden Silme İşlemi Gerçekleştirmek İçin: 5 
            
            """)

        işlem = input("Lütfen Gerçekleştirmek İstediğiniz İşlemi Seçiniz:")

        if(işlem == "1"):

            AEYS.envanter_göster()

            print("\n")
            işlem2 = input("Gerçekleştirmek İstediğiniz Başka Bir İşlem Var Mı ?: ")

            if (işlem2 == "E" or işlem2 == "e" or işlem2 == "Evet" or işlem2 == "evet"):
                print("\n")

            else:
                print("Askeri Envanter Yönetim Programından Çıkılıyor...")
                print("\n")
                print("GÜÇLÜ, CAYDIRICI, ETKİN !")
                AEYS.veritabanı_baglantı_kesme()
                break


        elif(işlem=="2"):

            print("Lütfen Bilgileri Giriniz !")
            print("\n")



            sistem_türü = input("Lütfen Sistemin Türünü veya Sınıfını Giriniz:")
            komutanlık = input("Lütfen Sistemin Bağlı Bulunduğu Komutanlığı Giriniz:")
            sistem_ismi = input("Lütfen Sistemin İsmini Giriniz:")
            envanter_giriş = input("Lütfen Sistemin Envantere Giriş Tarihini Giriniz:")
            miktar = input("Lütfen Sistemin Envanter Sayısını Giriniz:")
            durum = input("Lütfen Sistemin Envanter Durumunu Giriniz:")
            print("Sisteme Yükleniyor...")
            print("\n")
            time.sleep(2)
            AEYS.envanter_bilgi_ekleme(sistem_türü,komutanlık,sistem_ismi,envanter_giriş,miktar,durum)

            print("\n")
            işlem2 = input("Gerçekleştirmek İstediğiniz Başka Bir İşlem Var Mı ?: ")

            if (işlem2 == "E" or işlem2 =="e" or işlem2 == "Evet" or işlem2=="evet"):
                print("\n")

            else:
                print("Askeri Envanter Yönetim Programından Çıkılıyor...")
                print("\n")
                print("GÜÇLÜ, CAYDIRICI, ETKİN !")
                AEYS.veritabanı_baglantı_kesme()
                break


        elif(işlem =="3"):
            print("Lütfen Detaylı Bilgi Almak İstediğiniz Sistem İsmini Giriniz:")
            time.sleep(1)
            print("\n")
            sistem_ismi = input("Sistem İsmi:")
            print("\n")
            time.sleep(1)

            AEYS.envanter_sorgulama(sistem_ismi)

            print("\n")
            işlem2 = input("Gerçekleştirmek İstediğiniz Başka Bir İşlem Var Mı ?: ")

            if (işlem2 == "E" or işlem2 == "e" or işlem2 == "Evet" or işlem2 == "evet"):
                print("\n")

            else:
                print("Askeri Envanter Yönetim Programından Çıkılıyor...")
                print("\n")
                print("GÜÇLÜ, CAYDIRICI, ETKİN !")
                AEYS.veritabanı_baglantı_kesme()
                break

        elif(işlem == "4"):

            print("Envanter Veritabanı İçerisinden Silme İşlemi Gerçekleştirmek İçin Lütfen Bilgileri Giriniz:")
            print("\n")

            d3 = input("Lütfen Değiştirmek İstediğiniz Bilginin Sütun İsmini Giriniz:")
            d4 = input(("{} Sütununda Şuan Bulunan Bilgiyi Giriniz:".format(d3)))
            time.sleep(1)
            print("\n")

            d1 = input("Lütfen Değiştirmek İstediğiniz Bilginin Sütun İsmini Giriniz:")
            time.sleep(1)
            d2 = input("{} Sütununda Girmek İstediğiniz Yeni Bilgiyi Giriniz:".format(d1))
            print("Askeri Envanter Yönetim Programı Veritabanı Güncelleniyor...")
            time.sleep(1)

            AEYS.envanter_güncelleme(d1,d2,d3,d4)

    else:

        print("Askeri ID Numarası veya İsim Yanlış Girildi.")
        time.sleep(1)
        print("Lütfen Yeniden Deneyiniz ! " )
        print("\n")




