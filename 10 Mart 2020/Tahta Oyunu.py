# Tahta Oyunu - Bir oyun tahtasında ilerleme
# TBY414 - 10.03.2020

from random import seed
from random import randint

konumlar = [(3,4) , (5,6), (9,2), (4,6), (2,5), (5,5), (3,6), (3,8), (1,3), (2,5), (4,5)]
print(konumlar)
konumlar.append( (1,1))
print(konumlar)
ek_konumlar = [(2,4), (3,3)]
konumlar.extend(ek_konumlar) # listenin sonuna diğer listedeki elemanları ekledi
# konumlar.append(ek_konumlar) # Bu hatalı.
print(konumlar)
print("Tahtada toplam ", len(konumlar), " adet konum var.")

konum = 0
boyut = len(konumlar)
while konum < boyut:
    print("Mevcut konum: ", konumlar[konum])
    tahmin = int( input("İlerlemek için bir tahminde bulunun. Durmak için 0.") )
    if tahmin == 0:
        print("Durmaya karar verdik.")
        break
    else:
        seed(tahmin)
        adim = randint(0,5)
        konum = konum + adim
        print(adim, "adım ilerlenecek.")
        if konum >= boyut:
            konum = boyut - 1            
            print("Tahtanın sonuna geldik. Oyun bitti.")
            break
            # Bu break komutu olmadan da döngüden çıkar mıydı?
# Döngüden çıkıldı

print("Son konum: ", konumlar[konum])