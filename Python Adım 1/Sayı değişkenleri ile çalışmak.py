# İşleçlerin önceliğinden bahsetmiştik.
a = 1
b = 2
a = a * b + 7
# Burada çarpma işlemi olan * önceliklidir.
print ("a: ", a)

a = 9 / 3 + 2 * 4
# toplamanın solundaki bölme ve sağındaki çarpmanın ikisi de
# toplamaya önceliklidir. 
print ("a: ", a)
# Ancak çıktıya dikkat edin. 11.0 geldi, yani ondalıklı bir sayı oldu.

# Python'da bölme işlemi daima ondalıklı sonuç üretir
a = 8 / 2
print ("a: ", a)
a = 7 / 2
print ("a: ", a)
a = 7 / 1
print ("a: ", a)

#Ondalıklı sayılar ile çalışmanın bir yolu da kullanılan sabitlere ondalık eklemektir.
a = 8.0 + 2
print ("a: ", a)

# Tam sayılara int, ondalıklı sayılara float adını veriyoruz.
# Birisinden ötekine dönüşüm yapmak için da bu isimlere sahip
# işlevleri kulanıyoruz.
a = float (5)
print ("a: ", a)
a = int(6.0)
print ("a: ", a)

# Öte yandan ondalıklı bir sayının ondalık hanesi int dönüşümünde kaybedilir.
# Bu dönüşüm sayının negatif olmasından etkilenmez.
a = int (5.1)
print ("a: ", a)
a = int (-5.1)
print ("a: ", a)

# Yuvarlamak için kullandığımız round() işlevi de benzeri biçimde çalışır. 
a = 2.3435
ra = round(a)
print("a: ", a, " ra: ",ra)
a = -2.3435
ra = round(a)
print("a: ", a, " ra: ",ra)
