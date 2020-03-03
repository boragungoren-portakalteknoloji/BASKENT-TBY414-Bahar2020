# Beden kütle indeksi - Sağlık göstergesi hesaplama
# TBY414 03.03.2020

# ADIM 1 - Kullanıcı girdilerinden indeksi hesaplamak
# ağırlık (kg) boy (metre) olacak şekilde bki = a/(b*b)
agirlik = float( input("Lütfen ağırlığınızı giriniz (kg): ") )
#         ^ bir sayı olması gereken bir girdi alıyoruz.
boy = float( input("Lütfen boyunuzu giriniz (cm):") )
boy = boy / 100.0  # metreye çevirdik
bki = agirlik / (boy * boy)
print("BKİ değeri: ", bki)

# ADIM 2 - Kullanıcının sınıflandırmasını yapmak
# <18.5  <25     <30       <35     <40     --
# zayıf sağlıklı az kilolu 1. obez 2. obez 3. obez 
if bki <18.5:
    print("Zayıfsınız")
    print("Sağlıklı biçimde kilo alabilirsiniz")
    if boy<1.40:
         # Belki de çocuk?
         print("Çocuklar için BKİ formülü farklıdır.")         
elif bki < 25:
    print("Sağlıklısınız")
elif bki <30:
    print("Az kilolusunuz")
elif bki<35:
    print("Dikkat! 1. Obez")
elif bki<40:
    print("Dikkat! 2. Obez")
else:
    print("Dikkat 3. Obez")
    
# ADIM 3 - Bir kilo alma/verme hedefi oluşturmak
# Bu aynı zamanda ikinci ödevin bir parçası. 
# Not: Birinci ödev github hesabı açamak idi.


