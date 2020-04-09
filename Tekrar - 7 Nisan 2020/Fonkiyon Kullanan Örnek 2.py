def sagdakinikopar(butun, orta):
    parcalar = butun.split(orta)
    sag = parcalar[1]   
    return sag

# lambda suzgec: suzgec != haric
# Şuna benzer bir fonksiyonu otomatik üretir
# def esitdegilmi(suzgec, haric):
#    return suzgec != haric


def filtrelitopla(liste, filtre=""):
    # Metin işlemleri için - https://docs.python.org/3/library/string.html
    toplam = 0
    adimlayici = None
    if "!=" in filtre:
        # parcalar = filtre.split("!=")
        # haric = int( parcalar[1] )
        haric = int ( sagdakinikopar(filtre, "!=") )
        adimlayici = filter(lambda suzgec: suzgec != haric, liste)
                              # ^ bize true/false dönen basit bir fonksiyonu otomatik yarattı
                      # ^ filter, o fonksiyonu kabul kriteri yaparak, listeyi süzdü
        # ^ adımlayıcı, o filtre ile süzülmüş bir listeye bakıyor.            
        # iterator
    elif ">=" in filtre:
        sinir = int ( sagdakinikopar(filtre, ">=") )
        adimlayici = filter(lambda suzgec: suzgec >= sinir, liste)
    elif "<=" in filtre:
        sinir = int ( sagdakinikopar(filtre, "<=") )
        adimlayici = filter(lambda suzgec: suzgec <= sinir, liste)
    elif "<" in filtre:
        sinir = int ( sagdakinikopar(filtre, "<") )
        adimlayici = filter(lambda suzgec: suzgec < sinir, liste)
    elif ">" in filtre:
        sinir = int ( sagdakinikopar(filtre, ">") )
        adimlayici = filter(lambda suzgec: suzgec > sinir, liste)
    else:
        # Varsayılan değer boş, filtre yok olarak anlıyoruz
        adimlayici = iter(liste)
    # Artık adımlayıcımız var. 
    suzulmus = list (adimlayici)
    toplam = sum (suzulmus)
    return toplam
    
listem = [0, 1, 2, 3, 4, 5]

# Fonksiyon çağrılırken parametrelerin isimleri belirtilmeyenleri,
#tanımdaki sıra ile soldan sağa sıra ile eşleşmelidir
sonuc = filtrelitopla(listem, "!=5")
print(sonuc)
# Genellikle sırası eşleşse bile kod içinde anlamak kolaylaşsın diye
# bazı parametrelerin isimleri belirtilir
sonuc = filtrelitopla(liste=listem, filtre="<3")
print(sonuc)
sonuc = filtrelitopla(liste=listem, filtre="<=3")
print(sonuc)
# Fonksiyon çağrılırken parametrelerin tamamının ismi belirtilmiş
# ise sırası önemli değildir. 
sonuc = filtrelitopla(filtre=">4", liste=listem)
print(sonuc)
sonuc = filtrelitopla(filtre=">=4", liste=listem)
print(sonuc)
# Varsayılan değeri bulunan bir parametre için değer girilmezse
# varsayılan değeri ile çalışacaktır. 
sonuc = filtrelitopla(listem)
print(sonuc)


