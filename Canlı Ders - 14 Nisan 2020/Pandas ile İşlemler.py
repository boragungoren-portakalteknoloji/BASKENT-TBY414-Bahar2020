import pandas as pd
import numpy as np
import os
dosyaadi = os.getcwd() + "\\Kahve siparişleri.txt"
df = pd.read_csv(dosyaadi)
# ^ dataframe nesnesi, veri tablo halinde organize. Sütunlar halinde 
print(df)
#print(df.axes)
#print(df.index)
#print(df.columns)

### Tek tek sütunlara erişim
##print(df["Ad"]) # Pandas için tek tek kolonlara Series deniyor. 
##print("Büyüklük:", df.Ad.size, " , içeriğin türü", df.Ad.dtype )
###                   ^ df.Ad ile df["Ad"] arasında fark yok
print("Eşsiz isimler:", df.Ad.unique())
##print("Frekanslar:", df.Ad.value_counts())
##
##
##print("Kahve tüketimi")
##print("Ortalama:", df.Kupa.mean())
##print("İlk iki satır:")
##print(df.Kupa.head(2) )
##print("Son iki satır:")
##print(df.Kupa.tail(2) )
##
##kahve_array = np.asarray(df.Kupa)
#               ^ Pandas'a göre yazılmamış, direkt array veya list kullanan
#                 kitaplıklar için veri dönüşümü. 
##print(kahve_array)
##
print( df.groupby("Ad")["Kupa"].sum() )
#             ^ Filtre her bir "Ad" eşsiz değeri için gruplara ayır
#                        ^ Her grup için "Kupa" kolonunu seç
#                                ^ seçilen kolonun toplamını ver


