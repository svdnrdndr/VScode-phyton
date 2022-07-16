"""

havaYagisliMi = False
havaSogukMu = True
if havaYagisliMi==True:
    if havaSogukMu==True:
        print("lütfen şemsiye al ve gocuk giy")
    else:
        print("lütfen şemsiye al ve gocuk giymene gerek yok")
else:
    if havaSogukMu==True:
        print("şemsiye almana gerek ama gocuk giy")
    else:
        print("şemsiye almana gerek ve gocuk da giymene gerek yok")
"""
"""
snotu1=int(input("1.sinav notu giriniz\t:"))
snotu2=int(input("2.sinav notu giriniz\t:"))
ortalama=(snotu1+snotu2)/2
if ortalama>=85:
    print(f"{ortalama}yıl sonu başari notudur,başari durumu pekiyi")
elif ortalama>=70:
    print("başari durumu iyi")
elif ortalama>=55:
     print("başari durumu orta")
elif ortalama>=45:
     print("başari durumu geçer")
else:
    print("geçemez")
"""

"""sayi1,sayi2= int(input("1. sayı giriniz\t: ")), int(input("2. sy giriniz\t: "))
if sayi1 < sayi2:
    print(f"{sayi1}<{sayi2}")
elif sayi1> sayi2:
    print(f"{sayi1}>{sayi2}")
else:
    print(f"{sayi1}={sayi2}")"""
"""Lütfen Kullanıcı Adı Giriniz: user
Lütfen Kullanıcı Parolası Giriniz: 123
Hatalı Kullancı

Lütfen Kullanıcı Adı Giriniz: admin
Lütfen Kullanıcı Parolası Giriniz: 1234
Hatalı Parola

Lütfen Kullanıcı Adı Giriniz: admin
Lütfen Kullanıcı Parolası Giriniz: 123
Hoşgeldiniz Yönetici
"""


"""
adi,parola =int(input("lütfen kullanıcı adı giriniz")), int(input("lütfen kullanıcı parolası giriniz"))
if adi != admin:
    print("hatalı kullanıcı")
if parola !=123:
    print("hatalı parola") 
else print("hoşgeldin yönetici")
"""
"""kullaniciAdi = input("Lütfen Kullanıcı Adı Giriniz\t")
parola = int(input("Lütfen Kullanıcı Parolası Giriniz\t"))
if kullaniciAdi != "admin" :
        if parola == 123 :
            print ("kullanıcı adı yanlış. lütfen doğru kullanıcı adını giriniz")
else :
    if parola == 123 :
        print("hoşgeldiniz") 
    else :
        print ("parola hatalı. lütfen doğru parolayı giriniz")
"""
# nested if
# region ornek_1
"""
havaYagisliMi = False
havaSogukMu = False
i = 1
print("a")
if havaYagisliMi == True:
    if havaSogukMu == True:
        print("b")
    else:
        print("c")
else:
    if i == 0:
        print("d")
    else:
        print("e")
print("f")
"""
# endregion

# region ornek_2
"""
+   kullanıcı değer girecek
+   int dönüşümü yapılacak
+   kullanıcı 0 yada negatif değer girmemeli
+   0-100 arası yada 100+ olup/olmadığını bulan prog.
+   ekrana kullanıcı dostu çıktı verecek
"""
a = int(input("lütfen sayı giriniz \t : "))
if a > 0:
    if a < 100:
        print(f"{a} sayı 100 den küçüktür, pozitif")
    else:
        print(f"{a} sayı 100 den büyüktür, pozitif")
else:
    print("lütfen 0 yada negatif değer girmeyin")

# endregion