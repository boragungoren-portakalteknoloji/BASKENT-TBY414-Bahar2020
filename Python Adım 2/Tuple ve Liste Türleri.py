# Tuple ve Listeler Python'da veri işlemede en çok kullanılan iki veri türüdür.
# Bir Tuple, matematikteki vektör kavramı ile örtüşür.

koordinatlar = (1.0 , 1.0, 0.0)
print(koordinatlar)
print("İlk koordinat:", koordinatlar[0])
print("İkinci koordinat:", koordinatlar[1])
print("Üçüncü koordinat:", koordinatlar[2])

# Ancak tuple nesnelerinin önemli bir özelliği vardır. İçeriği değiştirilemez
# yani immutable nesnelerdir. Aşağıdaki satırdaki #'i kaldırdığınızda hata
# alacaksınız. 
#koordinatlar[0] = 2.0
# Gelen hata atama işleci olan = bu tür için geçersizdir anlamına gelen bir
# hatadır.
# Ancak burada bir kafa karışıklığı olmaması açısından, değişken ile ona
# erişirken kullandığımız değişken adı / referansın farklı şeyler olduğunu
# hatırlamakta yarar var. Aşağıdaki satırda hata yoktur. 
koordinatlar = (2.0, 1.0, 0.0)
# Bu satırda = işleci sağdaki tuple nesnesini alıp koordinatlar ismine
# bağlamaktadır.
# Hata alınan satırda ise = işleci 2.0 değerini alıp tuple nesnesinin
# içindeki bir alana yazmaya çalışıyordu.

# Liste türü ise, tuple'dan daha esnek bir türdür. Liste ardışık olarak
# "sıralanmış" (ordered) veriler anlamına gelir.
siparisler = [2, 3, 2, 5, 7, 7]
print(siparisler)
# Listelerin de indeks ile erişimi vardır.
print("İlk sipariş:", siparisler[2])
# Ancak liste nesneleri değiştirlebilirdir.
# İki siparişi birleştirmeye karar verdik. 
siparisler[0] = siparisler[0]+ siparisler[1]
siparisler.pop(1) # 1 indeksli olan siparişi sildik
print(siparisler)
# Başa başka bir dizi siparişten oluşan bir listeyi geçirdik
siparisler = [8, 9] + siparisler
print(siparisler)
# Sona başka bir sipariş listesini ekledik.
siparisler = siparisler + [6, 2, 3]
print(siparisler)
# Sona tek bir siparişi ekledik
siparisler.append(4)
print(siparisler)
# Başa tek bir siparişi ekledik
siparisler.insert(0,11) # Sıfır indeksli konuma 11'i ekle
print(siparisler)
# Üçüncü sıraya girecek şekilde bir siparişi ekledik.
siparisler.insert(2,19) # Üçüncü sıra yani 2 indeksli konuma 19'u ekle
print(siparisler)

# Önemli bir detay, Python tür ayrımı yapmadığı için hem tuple hem list
# içerisinde farklı türlerden veri saklanabilir.
adres1 = ("Bora", "Güngören", "bgungoren@baskent.edu.tr") # 3 adet veri içeren tuple
adres2 = ("Bora Güngören", "gbora@metu.edu.tr", 2) # farklı türde veriler içeren tuple
adresler_listesi = [adres1, adres2, "borag@metu.edu.tr", "bora@boragungoren.com"]
# 2 tuple ve 2 metin içeren liste
print(adresler_listesi)