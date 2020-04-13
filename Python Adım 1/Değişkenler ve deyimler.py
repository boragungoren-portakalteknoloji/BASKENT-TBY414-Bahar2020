# Python'da # karakteri not satırlarını belirtmek için kullanılır.
# Bir satırın başında # olursa o satır programın parçası değildir.
# Ancak not satırları programcının kendisi ve diğer programcılar
# için bıraktığı önemli notlardır.
# Profesyonel bir programcının programında normal kod satırı sayısı
# ile yakın sayıda, hatta daha fazla not satırı bulunur.

# Aşağıdakı satır programımızın ilk satırıdır. 
print("Merhaba bu bir Python programıdır.")
# ^ print işlevi parantezlerin arasındaki parametresini ekrana
#yazar.parantezlerden birisinin unutulması programın hata vermesine
# neden olur. Aşağıdaki satırın başındaki # işaretini silerek
# programı tekrar çalıştıracak olursanız, o satır için hata mesajı
# alacaksınız. 
#print("Merhaba bu bir Python programıdır."

# Bu arada print içerisinde, yani parantezlerin içinde yazan ve çift
# tırnak karakterleri arasında bulunan metin bir metin sabiti
# (İng. string literal) olmaktadır. Ekrana sabit mesajlar yazarken
# böyle yapıyoruz.

a = 5
print("a değişkeninin değeri: ", a)
#                              ^ print virgül ile ayırınca birden
# fazla şeyi yazabilir. Burada a yazdığımızda, print üstteki (daha
# önceki) satırlarda a olarak tanımlanmış bir şey arayacak.
# a = 5 satırında biz a'yı tanımlamıştık.
# Python bir değişken adı kullanılarak değer atamasını ilk gördüğü
# yerde, o değişkeni de tanımlar. Yani a = 5 diyerek, a'ya 5 değerini
# atamamız aynı zamanda a'yı da tanımladı.

a = "Bir metin değeri"
#  ^ Öte yandan atama işleci olan = değişkenin ne tür veri saklayacağı
# yönünde bir kısıtlamaya tabi değildir. Python'da değişkenlerin türü
# yoktur. Bir başka deyiş ile türleri değişkendir. 
# a değişkeni değeri başta 5 iken, sonra "Bir metin değeri" metin
# sabitine dönüştü. 
print("a değişkeninin değeri: ", a)

# Python'da değişkenlerin türünün serbestçe değişmesi, programcıya bazı
# esneklikler sağlar ancak acemi programcılar için de riskli olabilir.
# Bu nedenle yeni başlayanların değişkenlerin türünü keyfi olarak
# değiştirecek şekilde değer ataması yapmaktan kaçınması önerilir.

# Python programında tek başına çalışan tüm satırlara bir deyim
# (İng. statement) adı verilir. Python programları deyimlerden oluşur.
# Deyimin işletilmesi sonucunda bir değeri oluyorsa (buna geleceği),
# o deyime ifade (İng. expression) adı da verilir.

a = 2 + 3
#     ^ Burada + işareti, daha doğru deyiş ile işleci (İng. operator)
# solundaki ve sağındaki sayıların değerlerini toplar ve sonucu
# (yani 5 sayısını) döner (İng. return). Bir değer oluştuğu için
# 2 + 3 deyimi aynı azmanda bir ifadedir.
# Bu arada a değişkeninin değeri tekrar 5 oldu.
print("a değişkeninin değeri: ", a)

b = 2
a = b + 1
#     ^ Burada + işlecinin solunda b değişkeni, sağında 1 sayısı var.
# b değişkeni değeri 2, yani bir sayı olduğu için bu işlem sorunsuz
# sonuçlanır. İşlemin sonucu olan 3 değeri kalır.
# a = 3 gibi olur. Dolayısı ile sonuçta a değişkeni değeri 3 olur.
print("a değişkeninin değeri: ", a)

# Python kod satırlarında birden fazla işleç olduğu zaman hangisi önce
# çalışacak önemlidir. Bunun kuralları aslında sadedir.
# Şimdilik bir = yani atama (İng. assignment) işleci varsa, onun
# daima sağdaki iş ve işlemlerin bitmesini bekleyeceğini, en son kalan
# değeri kullanacağını bilmemiz yeterli.

a = a + 1
# Burada atama işleci önce sağ tarafı beklediği için, a değişkenin değeri
# sağ tarafta okunacaktır. En son 3 idi. O zaman 3 + 1, 4 olur.
# a = 4 gibi çalışır.
# değişkenin değerini 1 artırmak için bu şekilde yazılan kod son derece
# yaygın bir kod satırıdır.
print("a değişkeninin değeri: ", a)

# = dışındaki işleçler, esnek görünmekle birlikte aslında son derece
# sınırlı becerilere sahiptir.
# Aşağıdaki iki satıra bakın. 
b = "metin"
#a = b+1
# İkinci satırın başındaki # karakterini silerseniz, kod hata verecektir.
# Hata "must be str, not int" yani str olmalıydı, int değil şeklinde
# gelmektedir. Bu + işareti sağ tarafında 1 (sayı) yerine bir metin
# beklediği için oluyor.
a = b + "1"
# Yukarıdaki halinde ise kod çalışacaktır. Buna geri geleceğiz. 
print("a değişkeninin değeri: ", a)

# Python'da bir değişkenin değeri olmamasını isteyebiliriz.
# Bu ileride bir değere alacağı için yanlış kullanacağımız bir
# varsayılan değer vermekten kaçındığımız anlamına gelir.
# Bu amaçla None isminde özel bir değer kullanılır.

c = None
print("c'nin değeri:", c)

