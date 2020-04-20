# Yoklama - Öğrencilerin ad ve numaralarını kayda geçirir
# TBY414 - 10.03.2020
 
# Ad ve öğrenci noyu kullanıcıdan alıp bir tuple içine koymak 
#ad = input("Öğrenci adı:")
#no = int( input("Öğrenci no:")) 
#ogrenci = (ad, no)
#print(ogrenci)
 
# Tuple kullanan kodu temel alarak bir liste ile yoklama

yoklama = [] # içi boş liste
yanit = "e"
while yanit == "e":
    # öğrenci bilgisini alalım
    ad = input("Öğrenci adı:")
    no = int( input("Öğrenci no:")) 
    ogrenci = (ad, no)
    # yoklamaya ekleyelim
    yoklama.append(ogrenci)
    # devam edip etmeyeceğimizi soralım
    yanit = input("Devam edelim mi? e/h: ")
print("Yoklama: ", yoklama)
