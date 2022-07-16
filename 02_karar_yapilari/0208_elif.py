"""
s = int(input("lütfen iki basamaklı sayı değeri giriniz: "))
bSayisi = len(str(s))
if bSayisi>2:
    print("lütfen 2 basamaklı değer girin")
elif bSayisi<2:
    print("lütfen 2 basamaklı değer girin")
else:
    print(f"girilen {s} sayısının, onlar basamağı {s//10} ve birler basamağı {s%10}, basamakları toplamı {(s//10)+(s%10)}")
"""
#region elif
"""
havaDurumu = "serin"
print("a")
if havaDurumu == "yağmurlu":
    print("b")
elif havaDurumu == "sıcak":
    print("c")
else:
    print("d")
print("e")
"""
#endregion

#region ornek
"""
s = int(input("l. s. g : "))
if s>0:
    print("pozitif")
elif s<0:
    print("negatif")
else:
    print("sıfırdır")
"""
#endregion