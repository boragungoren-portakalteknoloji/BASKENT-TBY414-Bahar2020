# Soru 1
##a = 3.0
##b = 2.0
##c = 7
##d = a + b / c
##print ("d:", d)
##e = round(d)
##print("e:", e)
##f =float(e)
##print("f:", f)

# Soru 2
##isim ="Güngören, Bora"
##parcalar = isim.split(", ")
##isim_tuple = (parcalar[1], parcalar[0])
##liste = [isim_tuple, "bgungoren@baskent.edu.tr"]
##for nesne in liste:
##    print("Nesne:", nesne)

# Soru 3
##isimler = []
##isimler.append("Ahmet")
##isimler.append("Cem")
##isimler.append("Zafer")
##isimler.append("Sevilay")
##isimler.append("Işın")
##isimler.append("Yıldız")
##isimler.append("İlker")
##isimler.append("Bora")
##print("İsimler:", isimler)
##isimler.sort()
##print("İsimler:", isimler)

# Soru 4
##notlar = [80, 70, 80, 90]
##agirliklar = [20, 30, 30, 20]
##agirlikli = (notlar * agirliklar) / 400
##print("Ağırlıklı:", agirlikli)

# Soru 5
##import os
##dosya = os.getcwd() + "\\veriler.txt"
##dosya = open(dosya, "r")
##if dosya.readable() == True:
##    satir = dosya.readline()
##    # Çeşitli işlemler
##    dosya.close()
##else:
##    print("Okunamıyor")

# Soru 7
##def kare(x): #                               1
##    return x * x #                           2
##sayi = input("Bir sayı giriniz:") #          3
##sonuc = kare(sayi) #                         4
##print("Girdiğiniz sayının karesi:", sonuc) # 5

# Soru 8
##def selamla(isim="Yabancı", mesaj="Merhaba"):
##    print(mesaj, isim)
##    
##print("1")
##selamla("Bora")
##print("2")
##selamla()
