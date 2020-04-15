import os
# Dosya adı ve yol kavramları önemli
dosya = os.getcwd() + "\\Kahve siparişleri.txt" # Windows için \ -> \\, Diğerleri / 
#            ^ içinde bulunduğumuz çalşma dizinini veriyor (metin)
dosya = open(dosya, "r") # r okuma, w yazma, a sonuna ekleme
if dosya.readable() == True:
    satir = dosya.readline() # "Ad,Kupa\n" Burada \n satır sonu \r
    sutun_listesi = satir.split(",")
                    #  ^ split bana bir liste verecek ["Ad", "Kupa\n"]
    print("Sütunlar:", sutun_listesi)
    # Takip eden satırlar veri satırları
    for indeks in range(0,5): # Belirli sayıda satır okuyoruz.
        satir = dosya.readline()
        degerler = satir.split(",")
                # ^ liste olacak. ["Bora", "1\n"]
        print("Değerler:", degerler)
    dosya.close() # unutmuyoruz
else:
    print("Okunamıyor")

