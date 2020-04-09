def sagdakinikopar(butun, orta):
    #               ^ Bunun bir string olduğunu varsaydık
    # 1. örnek olarak butun = "!=5", orta="!="
    # 2. örnek olarak butun= "x!=5", orta="!="
    # 3. örnek olarak butun="Güngören,Bora" orta=","
    # 4. örnek olarak butun="x!=5!=8" orta="!="
    parcalar = butun.split(orta)
    # ^ bize string nesneleri olan bir liste geldi
    # 1. Örneğe göre ["", "5"]
    # 2. Örneğe göre ["x", "5"]
    # 3. Örneğe göre ["Güngören", "Bora"] - Bu program için uygunsuz bir girdi, "Bora" sayı değil.
    # 4. Örneğe göre ["x", "5", "8"]
    sag = parcalar[1]   # 0 indeksli soldaki, 1 indeksli sağdaki
    # 1. Örneğe göre parcalar[0] ise "", parcalar[1] "5"
    # 4. Örneğe göre parcalar[0] "x", parcalar[1] "5" ve parcalar[2] "8"
    # ^ listedeki her eleman string olacağına göre sag da string
    return sag
    #    ^  return ettiğimiz de string

def filtrelitopla(liste, filtre=""):
    # Metin işlemleri için - https://docs.python.org/3/library/string.html
    toplam = 0
    if "!=" in filtre:
        # parcalar = filtre.split("!=")
        # haric = int( parcalar[1] )
        haric = int ( sagdakinikopar(filtre, "!=") )
        #        ^ gelen string i int e dönüştürmem gerekiyor
        for sayi in liste:
            if sayi != haric:
                #  ^ burada sayi bir int olacağına göre haric de int olmalı
                toplam = toplam + sayi
    elif ">=" in filtre:
        sinir = int ( sagdakinikopar(filtre, ">=") )
        for sayi in liste:
            if sayi >= sinir:
                toplam = toplam + sayi
    elif "<=" in filtre:
        sinir = int ( sagdakinikopar(filtre, "<=") )
        for sayi in liste:
            if sayi >= sinir:
                toplam = toplam + sayi
    elif "<" in filtre:
        sinir = int ( sagdakinikopar(filtre, "<") )
        for sayi in liste:
            if sayi < sinir:
                toplam = toplam + sayi
    elif ">" in filtre:
        sinir = int ( sagdakinikopar(filtre, ">") )
        for sayi in liste:
            if sayi > sinir:
                toplam = toplam + sayi
    else:
        # Varsayılan değer boş, filtre yok olarak anlıyoruz
        for sayi in liste:
            toplam = toplam + sayi
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