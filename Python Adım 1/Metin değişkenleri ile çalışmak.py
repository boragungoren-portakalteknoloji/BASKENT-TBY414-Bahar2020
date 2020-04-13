isim = "Bora Güngören"
# Python'da metin değerleri, bir ipliğe dizilmiş
# boncuklar gibi görebileceğimi ardışık karakterlerden oluşur.
# Bu nedenle İngilizce iplik anlamına gelen String sözcüğü
# ile adlandırılırlar.

# Bir metindeki tüm karakterler sıralamada kaçıncı olduklarına
# göre tek tek erişilebilirdir. 
print(isim, " metninin ilk harfi: ", isim[0])
print(isim, " metninin ilk harfinden 1 sonraki harf: ", isim[1])
# Harflerin sıra numaraları ilk harften kaç harf sonra
# olduklarına göre verildiği için ilk harfin sıra numarası 0 olur.
# Biz bu sıra numaralarına indeks diyeceğiz.

# Bir metnin bütünü üzerinde işlemler yapabilen işlevler vardır.

bora = "bora"
bora = bora.capitalize()
# capitalize, metnin ilk karakterini büyük harf olarak değiştirir.
print("Capitalize sonrası, bora: ", bora)
# Tüm sözcüklerin ilk harfini büyütmek için ise title kullanılabilir.
bora = bora.title()
print("Title sonrası, bora: ", bora)

# Tek bir boşluk karakteri " " metni ile gösterilir
print("Boşluk öncesi-", " ", "-sonrası.")
# Burada print işletinin her bir metin arasına otomatik birer
# boşluk atması sonucu ekrandaki çıktıda 3 adet boşluk olacaktır.
# Biraz dikkat ederseni sayabilirsiniz. Ortadaki boşluk " "
# metninden gelendir. 

# Metinlerin arka arkaya bitiştirilmesi için + işareti
# kolaylıkla kullanılabilir.
bora = "bora" + " " +"Güngören"
print("Metin: ", bora)
bora = bora.capitalize()
print("Metin: ", bora)

# Metnin içeriğinde sadece basamaklar olup olmadığını anlamanın
# en kolay yolu isdigit fonksiyonudur.
# Ancak isdigit ondalık karakterlerini tanımaz, bu nedenle
# isdigit kullanarak tam sayı kontrolü yapabilirsiniz ama
# ondalıklı kontrolü yapamazsınız.
# Benzer kontroller için isnumeric ve isdecimal işlevleri de kullanılır.
metin = "12345"
print(metin, " için test ediyoruz")
print(metin, " basamaklardan mı oluşuyor?", metin.isdigit())
print(metin, " sayı karakterlerinden mi oluşuyor?", metin.isnumeric())
print(metin, " ondalık basamaklarından mu oluşuyor?", metin.isdecimal())

metin = "1234.5"
print(metin, " için test ediyoruz")
print(metin, " basamaklardan mı oluşuyor?", metin.isdigit())
print(metin, " sayı karakterlerinden mi oluşuyor?", metin.isnumeric())
print(metin, " ondalık basamaklarından mu oluşuyor?", metin.isdecimal())

metin = "1234,5"
print(metin, " için test ediyoruz")
print(metin, " basamaklardan mı oluşuyor?", metin.isdigit())
print(metin, " sayı karakterlerinden mi oluşuyor?", metin.isnumeric())
print(metin, " ondalık basamaklarından mu oluşuyor?", metin.isdecimal())

# Sıradan sayı değerleri için üçü arasında fark yoktur.
# Ancak isnumeric Çince, vb değişik dillerdeki basamak karakterlerini de
# kabul ederken, isdecimal sadece Latin alfabelerindeki 0,1,2,...,9 kabul
# edecektir. Ayrıca her ikisi de kare işareti, 1/2 gibi önceden oluşturulmuş
# sayı ifade eden özel karakterleri de kabul edecektir.
# Öte yandan isdecimal kare işareti gibi karakterleri kabul etmez. 

# İleride sütunlar halinde organize edilmiş dosyalar ile çalışırken
# Bir sütuna ortalanmış metin üretmek ihtiyacımız olabilir.
# Sütun genişliği metinden uzun ise, metnin sağına ve soluna doğru
# sayıda boşluk eklemek için kolay bir işlev vardır.
bora = "bora"
orta = bora.center(24)
print("Ortalanmış metin:", orta)

# Öte yandan, bir metnin başında ve sonundaki boşluk karakterlerinden
# kurtulmak da isteyebiliriz. Bu durumda strip işlevini kullanabiliriz.
temiz = orta.strip()
print("Ortalanmış metin:", orta, " temizlenmiş hali:", temiz)

# Kendiniz daha fazla metin işlevini incelemek isteyebilirsiniz.
# Özellikle ilginizi çekebilece olanlar startswith, endswith, isalpha,
# isalnum, isspace, lower, upper işlevleridir.
# İleride split işlevini ayrıca göreceğiz. 