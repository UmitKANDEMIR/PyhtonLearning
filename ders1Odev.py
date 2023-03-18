# Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

    #Veri Tipler:
        #String (metin) veri tipleri => str  
            #Metinsel ifadeler temsil etmektedir. Kullanım şekli ise " " veya ' ' şeklindedir. 
            #x = "Hello World" => str örneği
        #Numerik (sayısal) veri tipleri => int, float, complex 
            #Sayısal ifadeleri temsil etmektedir. İntegers ifadelerde tırnak kullanılmaz. kendi içerisinde ondalık veya tam sayı olmasına göre kategorilendirilir. int=>tam sayı float=>ondalık sayı demektir.
            #x = 2 => int
            #x = 1.5 => float
        #Sequence(sıralama) veri tipleri => list, tuple, range
            #Bu veri tipi bize verilerimizi kategorilere ayırarak bir arada tutmamızı sağlar. Örneğin bir okulda bir çok sınıf vardır ve bu sınıflarda öğrenciler vardır. her bir sınıf bir öğrenci listesi tutar.
            #x = ["Ahmet Saz", "Duygu Reçber" vb...] => list
            #x = range (8) => range çıktı olarak range (0,8) alırız.
            #x = ("banana", "apple", [1, "Ali", 8]) => tuple demet demektir. Tuple ile liste arasındaki fark liste üzerinde değişim yapabilirken tuple üzerinde bir değişm yapamıyoruz.
        #mapping(haritalama) veri tipleri => dict
            #x = {"name" : "Umit", "age" : 25} => dict Dict yapıları sıralanamaz ancak liste elemanlarına key ve value değerlerine göre ulaşıp elemanlar üzerinde güncelleme yapabiliriz. 
        #Set veri tipleri => set,frozenset
            #x = {"apple", "banana", "cherry"} => set Küme demektir. Liste, sözlük ve demet veri türü gibi birden çok veri türünü birlikte barındıran veri tipidir.Kümeler ile ilgili yaptığınız her türlü işlevi(birleşme,kesişim vs.) bu veri tipi ile yapabilirsiniz.
            #x = frozenset({"apple", "banana", "cherry"}) Immutable(değiştirilemez) veri tipidir. Değişmez bir set oluşturmak için kullanılır.
        #Boolean veri tipleri => bool
            #mantıksal ifade içeren veri tipidir. TRUE veya FALSE içerir sadece.
            #x = True
        #Binary veri tipleri => bytes, bytearray, memoryview 

# Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

    #str => websitesindeki bütün metinsel ifadeler
    #int => websitesindeki bütün sayısal ifadeler
    #bool => kurslardaki bitir ve devam et kısımı
    # list => ana sayfada bulunan kurslar, kategori barı, eğitmen barı


# Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

#if-else => bitir devam et ile dersi tamamlama yüzdesi ve giriş yap kısmı
bitirVeDevamEt = False
if  bitirVeDevamEt:
    print("Ödev Başarıyla Tamamlandı")
else:
    print("Ödev Tamamlanamadı")
#for => eğitmenler kısmında eğitmeni seçtiğimizde o kişinin kurslarının gelmesi

kurslar = (["Pyhton","C#2023"],["C#", "Java", "Javascript"])
egitmenler = ["Enes", "Mehmet"]
enes = kurslar[0]
mehmet = kurslar[1]
egitmenAdi = input("Eğitmen Adı: ")

for kurs in kurslar:
    if egitmenAdi == egitmenler[0]:
        print(enes)
        break
    else:
        print(mehmet)
        break 