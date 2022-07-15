

"""
ogrenciAdi=["ali","kemal","mehmet","mustafa"]
while true:
    ogrenciAdi= input("aradığınız öğrenci giriniz, çıkmak için ç: ")
    if ogrenciAdi=="ç":
        break
    """


   
"""
    oListesi = ["sevdanur", "halil", "berkan", "sevda", "aziz","tolga", "oğuz"]
arananOgrenci = input("aramak istediğiniz öğrenci: ")
i = oListesi.index(arananOgrenci)
if i>=0:
    print(f"listede {arananOgrenci} var")
"""

"""
oListesi = ["sevdanur", "halil", "berkan", "sevda", "aziz","tolga", "oğuz"]
#print("halildfghjk" in oListesi)
arananOgrenci = input("aramak istediğiniz öğrenci: ")
if arananOgrenci not in oListesi:
    print(f"{arananOgrenci} listede yoktur")
else:
    print(f"{arananOgrenci} listede var, listenin {oListesi.index(arananOgrenci)+1}. sıradaki öğrencidir")



# if arananOgrenci in oListesi:
#     print(f"{arananOgrenci} listede var")
# else:
#     print(f"{arananOgrenci} listede yoktur")
"""

"""
sehirListesi=["konak","karşıyaka","menemen"]
istenenSehir= input("istenen sehir: ")
if istenenSehir in sehirListesi:
    print(f"{istenenSehir} listede var, listenin {sehirListesi.index(istenenSehir)+1}. sehirdir")
else:
    print(f"{istenenSehir} yoktur.")
    """



'''
ilceler=[]

while True:
    ilce =input("ilçe giriniz,çıkmak için -1: ")
    if ilce=="-1": 
        break
    ilceler.append(ilce)
print(ilceler)
'''

"""
ilceler = "TUZLA MALTEPE BEBEK BEYLİKDÜZÜ"
# print(f"{ilceler.count(' ')} adet ilçe var")
# for i in ilceler:
#     if i==" ":
#         print()
#     print(i,end="")



# listem = list(range(0,10))
# print(listem)


for i in range(0, len(ilceler)):
    if ilceler[i]==" ":
        print()
        i+=1
        continue
    print(ilceler[i],end="")

"""

# liste = [i for i in range(1,9)]
# liste = [i*i for i in range(1,9)]
# liste = ["piyon" for i in range(1,9)]
# print(liste)

"""
hafaninGunleri = ["", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
liste= [f"haftanın {i}. günü {hafaninGunleri[i]}" for i in range(1,8)]
print(liste)"""
"""
Haftanın 1. Günü Pazartesi Haftanın 2. Günü Salı
"""
"""
o1 = ["Mustafa Erdem","Bilg.Müh",60,80]
o2 = ["Sevdanur Dündar","Biomedikal",90,100]
o3 = ["Aziz Bektaş","Bilg. Öğr",30,40]
ogrenciler = [o1,o2,o3]
ortalamalar=[]
#print(ogrenciler)
for ogrenci in ogrenciler:
   # print((ogrenci[2]+ogrenci[3])/2 )
    if (ogrenci[2]+ogrenci[3])/2 < 50:
        print(f"{ogrenci[0]} {ogrenci[1]} kaldı.")
    else:
        print(f"{ogrenci[0]} {ogrenci[1]} geçti.")"""
"""
o1 = ["Mustafa Erdem", "Bilg.Müh", 60, 70]
o2 = ["Sevdanur Dündar", "Biomedikal", 100, 100]
o3 = ["Aziz Bektaş", "Bilg. Öğr", 30, 40]
ogrenciler = [o1, o2, o3]
ortalamalar = []
for ogrenci in ogrenciler:
    ort = (ogrenci[2]+ogrenci[3])/2
    ortalamalar.append(ort)
genelOrt = round(sum(ortalamalar)/len(ortalamalar),2)



for ogrenci in ogrenciler:
    ort = (ogrenci[2]+ogrenci[3])/2
    if ort < genelOrt:
        print(f"{ogrenci[0]} {ogrenci[1]} {ort}→ kaldı.")
    else:
        print(f"{ogrenci[0]} {ogrenci[1]} {ort}→ geçti.")"""

print("kim\tkorkar\npyhtondan")
