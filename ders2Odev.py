ogrenciler = ["Ahmet Çalık", "Servet Çetin", "Ali Kılıç"]
def sonuc():
    print(ogrenciler)

# Aldığı isim soy isim ile listeye öğrenci ekleyen
def ogrenciEkle ():
    ogrenci = input ("İsim ve soyisim giriniz: ")
    ogrenciler.append(ogrenci)
    sonuc()
##Fonksiyonu çalıştır
#ogrenciEkle()  
## Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
def ogrenciSil ():
    ogrenci = input ("Kayıdı silinecek öğrenci isim ve soyadı: ")
    ogrenciler.remove(ogrenci)
    sonuc()
#ogrenciSil()
##Listeye birden fazla öğrenci eklemeyi mümkün kılan
def cokluOgrenciEkleme ():
    adet = input ("Kaç adet öğrenci eklenecektir: ")
    i = 0
    while i<int(adet) :
        ogrenci = input ("İsim ve soyisim giriniz: ")
        ogrenciler.append(ogrenci)
        if i == adet:
            break
        i +=1
    sonuc()
#cokluOgrenciEkleme()
##Listedeki tüm öğrencileri tek tek ekrana yazdıran
def ogrenciListesi():
    i=0
    lstAdt = len(ogrenciler)
    while i<lstAdt:
        print(ogrenciler[i])
        if i == lstAdt:
            break
        i +=1
#ogrenciListesi()
##Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
def ogrenciNu ():
    ogrenci = input("İsim ve soyisim giriniz: ")
    print(ogrenciler.index(ogrenci))
#ogrenciNu()
##Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
def cokluOgrenciSilme ():
    adet = input ("Kaç adet öğrenci silinecektir: ")
    i = 0
    while i<int(adet) :
        ogrenci = input ("İsim ve soyisim giriniz: ")
        ogrenciler.remove(ogrenci)
        if i == adet:
            break
        i +=1
    sonuc()
cokluOgrenciSilme()
