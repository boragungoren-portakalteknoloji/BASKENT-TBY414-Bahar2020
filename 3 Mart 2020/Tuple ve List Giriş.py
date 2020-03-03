# Tuple ve List giriş
# TBY414 03.03.2020

kimlik = ("Bora", "Güngören", "TBY414", "borag@metu.edu.tr", 1)
# tuple - boyutu tanımlandığı anda sabitlenen bir veri yapısı
print(kimlik)
print(kimlik[0])

kimlik = ["Bora", "Güngören", "TBY414", "borag@metu.edu.tr", 1]
# list - boyutu değişebilem (ekleme çıkarma yapılabilen) bir veri yapısı
print(kimlik)
print(kimlik[0])

olcumler = [100, 99, 98, 97 , 98 , 99]
for olcum in olcumler:
    print(olcum)