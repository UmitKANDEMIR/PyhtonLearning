# HTML => bir programlama dili sayılmaz çünkü web sayfaları için standart biçimlendirme dilidir.
# HTML LOCATORS => Selenium'da hangi web tabanlı objeler üzerinde çalışması gerektiğini söyleyen bir komuttur.
# SELENIUM'DA AKSİYONLAR => Selenium web arayüz testleri yapmak için web tarayıcılarına komut göndermeye yarayan bir kütüphanedir. Başlıca aksiyonlar şunlardır; web sayfalarına gitmek(.get), web sayafalarındaki inputlara kelimeler göndermek(.send_keys), web sayfalarında tıklamak(.click), enter tuşuna basarak arama yapması(Keys.RETURN), element bulması HTML kodlarından ve bu sayede üzerinde çalışacağımız objenin kolaylıkla bulunması (.find_element), sayfaları aşağı veya yukarı kaydırmak (Keys.PAGE_DOWN ve Keys.PAGE_UP)
# SELENIUM'DA KULLANILAN METOTLAR => * get(url): Belirtilen URL'yi yükler.
# * find_element_by_*(): Belirtilen seçici ile eşleşen ilk elementi bulur. Yıldız karakteri, farklı seçici türlerini ifade etmek için kullanılır. Örneğin:
#   * find_element_by_id(): ID seçicisine göre elementi bulur.
#   * find_element_by_name(): Name seçicisine göre elementi bulur.
#   * find_element_by_xpath(): XPath seçicisine göre elementi bulur.
#   * find_element_by_css_selector(): CSS seçicisine göre elementi bulur.
#   * find_elements_by_*(): Belirtilen seçici ile eşleşen tüm elementleri bulur. find_element_by_*() metodu gibi farklı seçici türleri için kullanılabilir.
# * send_keys(*keys_to_send): Belirtilen tuşları (veya metni) belirtilen elemente gönderir.
# * click(): Elemente tıklar.
# * clear(): Elementin içeriğini temizler.
# * get_attribute(name): Elementin belirtilen özelliğinin değerini döndürür. Örneğin, get_attribute("value") bir input elementinin değerini döndürür.
# * text(): Elementin metin içeriğini döndürür.
# * submit(): Formu gönderir.
# * back(): Tarayıcıda bir önceki sayfaya döner.
# * forward(): Tarayıcıda bir sonraki sayfaya gider.
# * refresh(): Sayfayı yeniler.