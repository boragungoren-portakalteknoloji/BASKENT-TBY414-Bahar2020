# Duruma göre kod - if else

# Belirli bir durum geçerli ise çalışacak kod

yas = int( input("Yaşınız kaç: ") )
# Sadece kullanıcı ergen ise çalışacak kod?
if yas < 18:
    # bu satır bir tab girintili ÖNEMLİ
    print("Yaşınız itibarı ile ergensiniz.")

print("Normal akışa döndük")

if yas > 65:
    print("Saygılar.")
else:
    print("Merhaba.")

print("DSÖ'ye göre...")
if yas < 18:
    print("Ergen.")
elif yas <= 65:
    print("Genç")
elif yas <=74:
    print("Orta yaşlı")
elif yas <85:
    print("Yaşlı")
else:
    print("Çok yaşlı")


    


