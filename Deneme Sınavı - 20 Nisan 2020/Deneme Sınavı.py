# Deneme Sınavı 20.04.2020

# Soru 1 Kullanıcı girdisi alırken formatlama
##isim = input("Lütfen isminizi giriniz.")               # 1
##yas = input("Lütfen yaşınızı giriniz")                 # 2
##if yas < 18:                                           # 3
##    print("Sevgili", isim, "18 yaşından küçüksünüz.")  # 4
##else:                                                  # 5
##    print("Sayın", isim, "18 yaşından küçük değilsiniz.") # 6
    
# Soru 2 ve 3 Girintileme kuralları
##a = 4 # 1
##b = 5 # 2
##if a * a < 4 * b: # 3
##    print("anın karesi küçükmüş.") # 4
##print("küçük olmasının işlemleri") # 5
##else: # 6
##    print("anın karesi büyükmüş") # 7
##    print("büyük olmasının işlemleri") # 8

# Soru 4 ve 5 None değeri
##deger1 = None
##deger2 = int( input("Lütfen bir tamsayı giriniz.") )
##if deger2 < 0:
##    print("Negatif bir sayı")
##    deger1 = -deger2
##else:
##    print("Pozitif bir sayı.")
##print("Değer 1:", deger1)

import pandas as pd
dosyaadi = os.getcwd() + "\\dosya.txt"
df = pd.read_csv(dosyaadi)
print(df)
