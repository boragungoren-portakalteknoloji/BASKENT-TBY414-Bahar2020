# Basit Hesaplar -- Dört işlemi görselleştirir
# TBY414 03.03.2020 Bora Güngören

a = 3
b = 4
c = a + (b-2) * (b+2)
# Matematikteki işlem önceliği kuralları geçerlidir. 
print("İşlem sonucu: ", c)
d = (-1 * c) / 2
print("Bölme işlem sonucu: ", d)
e = int (d)
print("Tam sayıya dönüşmüş hali: ", e)
# Sadece tam kısmı alınır 7.5 -> 7, -7.5 -> -7
f = round(d)
# Büyüklüğü yuvarlanır, işareti korunur
print("Yuvarlanmış hali", f)

g = None
print("İçi boş değişken: ", g)
h = g + 1


