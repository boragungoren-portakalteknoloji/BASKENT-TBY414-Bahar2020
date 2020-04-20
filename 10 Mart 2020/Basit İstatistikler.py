# Basit İstatistikler
# TBY414 - 10.03.2020

sayilar = []
print("1-10 arasında sayılar girin. Durmak için 0 girin.")
sayi = 1
while sayi != 0:
    sayi = int( input("Sıradaki sayı: "))
    if sayi == 0:
        break
    else:
        sayilar.append(sayi)
print("Girilen sayılar:", sayilar)

toplam = 0
for sayi in sayilar:
    toplam = toplam + sayi
print("Tek tek topladığımızda toplam:", toplam)
diger_toplam = sum(sayilar)
print("Sum işlevi ile topladığımızda toplam:", diger_toplam)

n = len(sayilar)
ortalama = toplam / n
print("Ortalama: ", ortalama)

from statistics import mean
print("Ortalama: ", mean(sayilar))

