import random 

# şehir sınıfı
class Sehir():
    sehirIsimListesi = []
    def __init__(self, isim):
        self.isim = isim
        self.canavarVar = True
        self.kumarhaneVar = False
        self.tuccarVar = False
        self.evVar = False
        self.sehirIsimListesi.append(self.isim)
        self.gidSehirLis = []  # gidilebilir şehir listesi
        self.karakterler = []      # içindekiler karakter referansları olacak
        self.karakterIsimListesi = []  # içindekiler string olacak
        self.canavarlar = []
        self.canavarIsimListesi = []
    def baglantiEkle(self, komsuSehir):
        self.gidSehirLis.append(komsuSehir.isim)
    def karakterEkle(self, karakter):
        self.karakterler.append(karakter)
        self.karakterIsimListesi.append(karakter.isim)
    def karakterleriListele(self):
        if len(self.karakterler) == 0:
            print("Kahraman : Çevrede konuşulacak herhangi bir şey yok")
        else:
            print("Diyaloğa Girebileceğin Karakterler : ")
            for kar in self.karakterler:
                print(kar.isim)
    def canavarEkle(self, canavar):
        self.canavarlar.append(canavar)
        self.canavarIsimListesi.append(canavar.isim)
    def canavarListele(self):
        for canavar in self.canavarIsimListesi:
            print("Canavarlar : \n", canavar)

# canavar sınıfı
class Canavar():
    def __init__(self, isim, seviye, silah, silahHasari):
        self.isim = isim
        self.seviye = seviye
        self.guc = 1
        self.beceri = 1
        self.ceviklik = 1
        self.silah = silah
        self.silahHasari = silahHasari
        self.zirh = "yok"
        self.verdigiDeneyim = 10
    def ol(self, kahraman):
        print(self.isim , " öldü")
        altin = random.randint(0, 5)
        print(kahraman.isim , " ", altin, " altin kazandı")
        print(kahraman.isim , " ", self.verdigiDeneyim, " deneyim kazandı" )
        kahraman.altin += altin
        kahraman.deneyimPuani = self.verdigiDeneyim

# karakter sınıfı
class Karakter():
    def __init__(self, isim):
        self.isim = isim
        self.ilkKonusma = ""
        self.diyalog = "" 
    def selamla(self):  # ismi aldatmasın ilk konuşmayı yapacak fonksiyon
        print(self.ilkKonusma, end="")
    def diyalogaGir(self, kahraman):
        self.selamla()
        cevap = input("\n(Kabul ediyorsan Kabul yaz)\n")
        if cevap.strip().lower() == "kabul":
            kahraman.altin -= 10
            kahraman.bulunduguYer = sehirListesi[1]
            print("Petra şehrine ışınlandın")
        else:
            print("Işınlanma gerçekleşmedi")



# canavarlar
c1 = Canavar("kurt", 1, "sağlam çene", 1)

# karakterler
movia = Karakter("movia")
movia.ilkKonusma = "Movia -Eğer Petra şehrine dönmek istiyorsan bana 10 altın ödemek zorundasın! "

sehirListesi = [Sehir("shire"), Sehir("petra"), Sehir("mitra"), Sehir("aisan"), Sehir("hazar")]
sehirListesi[4].karakterEkle(movia)

#şehir bağlantılarını düzenleyelim
sehirListesi[0].baglantiEkle(sehirListesi[1]) # shire şehrinden petraya gidilebilir
sehirListesi[1].baglantiEkle(sehirListesi[0]) # petra şehrinden shire şehrine gidilebilir
sehirListesi[1].baglantiEkle(sehirListesi[2]) # petra şehrinden mitra şehrine gidilebilir
sehirListesi[1].baglantiEkle(sehirListesi[3]) # petra şehrinden aisan şehrine gidilebilir
sehirListesi[1].baglantiEkle(sehirListesi[4]) # petra şehrinden hazar şehrine gidilebilir
sehirListesi[2].baglantiEkle(sehirListesi[1]) # mitra şehrinden petra şehrine gidilebilir
sehirListesi[3].baglantiEkle(sehirListesi[2]) # aisan şehrinden petra şehrine gidilebilir

# shire şehrinde canavar olmasın
sehirListesi[0].canavarVar = False

# shire şehrinde evimiz olsun
sehirListesi[0].evVar = True

# mitra şehrine kumarhane ekleyelim
sehirListesi[2].kumarhaneVar = True

# hazar şehrine canavar ekleyelim
sehirListesi[4].canavarEkle(c1)


# kahraman sınıfı oluşturalım
class Kahraman():
    def __init__(self, isim):
        self.isim = isim
        self.seviye = 1
        self.deneyimPuani = 0
        self.altin = 100
        self.susuzluk = 0
        self.aclik = 0
        self.uykusuzluk = 0
        self.guc = 2
        self.beceri = 1
        self.ceviklik = 2
        self.silah = "Yumruk"
        self.silahHasari = 10
        self.zirh = "yok"
        self.bulunduguYer = sehirListesi[0]
        print("Kahramanınız Oluşturuldu, ismi", self.isim)
    def git(self, gidilecekYer):
        for i in range(5):
            if gidilecekYer == sehirListesi[i].isim:
                break
        self.bulunduguYer = sehirListesi[i]
        print(sehirListesi[i].isim + " şehrine gidildi")
    def savas(self, canavar):
        if(self.bulunduguYer.canavarVar):
            for c in self.bulunduguYer.canavarlar:
                if canavar == c.isim:
                    break
            if c.silahHasari * c.guc * c.ceviklik > self.silahHasari * self.guc * self.ceviklik:
                c.ol(self)
            else:
                print("Kahraman öldü!")
        else:
            print("Burada savaşabileceğin bir canavar yok")
    def seviyeAtla(self):
        self.seviye += 1
        # başka özellikleri de güçlendiricem
    def konus(self, karakter):
        if karakter in self.bulunduguYer.karakterIsimListesi:
            for i in range(len(self.bulunduguYer.karakterIsimListesi)):
                if karakter == self.bulunduguYer.karakterIsimListesi[i]:
                    break
            self.bulunduguYer.karakterler[i].diyalogaGir(self)
        else:
            print("Bu şehirde böyle birisi yok!")
    def uyu(self):
        if self.uykusuzluk < 5:
            print("Kahramanının uykusu yok")

def komutIsle(komut, kahraman):
    if komut=="yardım":    
        print("""
Yardım Sayfası :
    Verebileceğiniz Komutlar:
        yardım                  -> yardım sayfasını açar
        git <şehir-ismi>        -> gitmek istediğiniz şehir ismi ile o şehire gidebilirsiniz
        savaş <canavar>         -> argüman olarak verdiğiniz canavar ile savaşırsınız
        durum                   -> kahramanınızın durumunu görüntülersiniz
        harita                  -> haritayı görüntüler
        konuş <karakter>        -> argümansız olarak kullanıldığında bulunduğun şehirde diyaloga girebileceğin kişileri listeler
        oyna <altın-miktarı>    -> şehirde kumarhane varsa gözden çıkardığınız para ile kumar oynarsınız
        uyu                     -> şehirde eviniz varsa uyursunuz, böylelikle dinlenirsiniz
        q                       -> oyundan çık""")

    elif "savaş" in komut:
        if komut == "savaş":
            print("Kiminle savaşmak istediğini belirtmen gerekiyor")
        else:
            kelimeler = komut.strip().split()
            savasilacak = kelimeler[1].strip()
            if not savasilacak in kahraman.bulunduguYer.canavarIsimListesi:
                print("böyle bir canavar burada yok")
            else:
                kahraman.savas(savasilacak)
    elif komut=="durum":
        print("Kahramanın\nIsmi :\t\t", kahraman.isim)
        print("Seviyesi :\t", kahraman.seviye)
        print("Deneyim Puani :\t", kahraman.deneyimPuani)
        print("Mevcut Altın :\t", kahraman.altin)
        print("Susuzluk : \t", kahraman.susuzluk)
        print("Açlık : \t", kahraman.aclik)
        print("Guc : \t", kahraman.guc)
        print("Ceviklik : \t", kahraman.ceviklik)
        print("Silah : \t", kahraman.silah)
        print("Bulunduğu Şehir :", kahraman.bulunduguYer.isim)
    elif komut=="oyna":
        if not kahraman.bulunduguYer.kumarhaneVar:
            print("Bu şehirde kumarhane yok")
        else:
            print("Bu şehirde kumarhane var")
            # kumar kodularını buraya yazıyoruz
    elif komut=="uyu":
        if kahraman.bulunduguYer.evVar:
            kahraman.uyu()
    elif "git" in komut:
        if komut!="git":
            kelimeler = komut.strip().split()
            gidilecekYer = kelimeler[1]
            if gidilecekYer in Sehir.sehirIsimListesi:
                if gidilecekYer == kahraman.bulunduguYer.isim:
                    print("Zaten oradasın")
                elif gidilecekYer in kahraman.bulunduguYer.gidSehirLis:
                    kahraman.git(gidilecekYer)
                else:
                    print("bulunduğun şehirden " + gidilecekYer + " şehirine doğrudan bağlantı yok")
                    print("harita görütülemek için 'harita' komutunu verin")
            else:
                print("böyle bir şehir bu oyunda mevcut değil")
        else:
            print("eksik argüman, git komutunu gitmek istediğin şehir ile birlikte yazmanız gerekiyor")
    elif komut=="harita":
       print("""Harita :
            Mitra
               *  
                \\  
                 \\  
                  *      
    Aisan  *-----*  Petra *----------*  Shire  
                    /
                   /
                  /
                 *
            Hazar

    * işareti ok ucu anlamındadır""")
    elif "konuş" in komut:
        if komut=="konuş":
            kahraman.bulunduguYer.karakterleriListele()
        else:
            kelimeler = komut.strip().split()
            konusulacakKisi = kelimeler[1].strip()
            kahraman.konus(konusulacakKisi)
    elif "canavar-listele" == komut:
        if kahraman.bulunduguYer.canavarVar:
            kahraman.bulunduguYer.canavarListele()
    else:
        print("! eksik ya da yanlış komut !")


print("Oyuna Hoşgeldiniz!\nYardım için : 'yardım' komutunu verin")
kahramanisimi = input("Kahramanınızın ismini giriniz : ")

khm = Kahraman(kahramanisimi)

while True:
    komut = input("> ")
    komut = komut.lower().strip()
    if komut == "q":
        break
    komutIsle(komut, khm)


    


