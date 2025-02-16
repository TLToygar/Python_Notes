#1-toyota, bmw, renault, mercedes elemanlı bir liste oluştur.
#2- liste kaç elemanlı?
#3- listenin ilk ve son elemanını çek
#4- renault markasını togg ile güncelle
#5-listenin ilk 2 elemanını al
#6-listenin sonuna ford ve citroen ekle 
#7-listenin son elemanını sil

#markalar = ["toyota", "bmw", "renault", "mercedes"]
#print(len(markalar))
#print(markalar)
#print(markalar[0], markalar[-1])
#markalar[2] = "TOGG"
#print(markalar)
#print(markalar[:2])
#markalar= markalar + ["ford", "citroen"]
#print(markalar)
#markalar.pop()
#print(markalar)
#Yakitlar {
 #   "benzin": 46.54,
  #  "lpg": 27.62,
   # "dizel": 46.61
#}
#Kosul ifadeleri - if, elif, else


#Sorular:
#1- Bir aracın (yakıt tipine göre) klavyeden belirtilen bir mesafede ne kadar yakıt tükkettiğini hesaplayan 
# uygulamayı yaz.
benzin = 46.54
lpg = 27.62
dizel = 46.61

yakit_tipi = input("Yakıt tipini giriniz: ")
tüketim = float(input("100Km'deki tüketimi giriniz: ")) 
mesafe = int(input("Mesafeyi giriniz Km: "))

kmBasinaYakilanYakit =  (tüketim / 100) 
toplamYakitTüketim = kmBasinaYakilanYakit * mesafe
toplamYakitTüketim = round(toplamYakitTüketim, 2)    
print("Toplam Yakıt Tüketimi: " + str(toplamYakitTüketim))
if yakit_tipi == "benzin":
    print("Ödemeniz gereken miktar: " + str(toplamYakitTüketim * benzin))
elif yakit_tipi == "lpg":
    print("Ödemeniz gereken miktar: " + str(toplamYakitTüketim * lpg))
elif yakit_tipi == "dizel":
    print("Ödemeniz gereken miktar: " + str(toplamYakitTüketim * dizel))
else:
    print("Geçersiz yakıt tipi")
    
