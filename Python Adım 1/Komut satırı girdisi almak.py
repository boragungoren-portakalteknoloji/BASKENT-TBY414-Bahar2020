# Python'da programların en temel çalışma ortamı komut satırıdır.
# Öğrenirken herkes belirli bir süre için komut satırını kullanır.
# Komut satırında kullanıcıdan girdi almak için input işlevi
# kullanılır.

isim = input("İsminiz nedir?")
print("isim: ", isim)

# input daima bir metin olarak değer döner. Bu nedenle sayıları
# elle dönüştürmek gerekir. Aksi takdirde işlemlere giremezler

sayi = input("Lütfen 3 girin:")
# ^ Değişken adı sayi olabilir ama bu değişkenin değeri
# şu anda bir metin. "3" gibi. 
sayi = int(sayi)
print("sayi:", sayi)
sayi = sayi + 2
# int() dönüşümü sayesinde işlemlerde hata yapmıyoruz
print("sayi:", sayi)

sayi = input("Lütfen 3.0 girin:")
# ^ Değişken adı sayi olabilir ama bu değişkenin değeri
# şu anda bir metin. "3" gibi. 
sayi = float(sayi)
print("sayi:", sayi)
sayi = sayi + 2
# int() dönüşümü sayesinde işlemlerde hata yapmıyoruz
print("sayi:", sayi)
