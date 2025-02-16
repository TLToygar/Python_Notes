#1-toyota, bmw, renault, mercedes elemanlı bir liste oluştur.
#2- liste kaç elemanlı?
#3- listenin ilk ve son elemanını çek
#4- renault markasını togg ile güncelle
#5-listenin ilk 2 elemanını al
#6-listenin sonuna ford ve citroen ekle 
#7-listenin son elemanını sil

markalar = ["toyota", "bmw", "renault", "mercedes"]
print(len(markalar))
print(markalar)
print(markalar[0], markalar[-1])
markalar[2] = "TOGG"
print(markalar)
print(markalar[:2])
markalar= markalar + ["ford", "citroen"]
print(markalar)
markalar.pop()
print(markalar)
