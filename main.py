# 1. Uygulama
ISIM = input("adınızı girin")
MAAS = float(input("maaşınızı girin"))
YIL = float(input("çalışma yılınız girin"))

if YIL >=0 and YIL <=5:
    MAAS+= (MAAS*0.13)
    print("Sayın {} zamlı maaşınız {} TL".format(ISIM , MAAS))
elif YIL >=6 and YIL <=10:
    MAAS+= (MAAS*0.20)
    print("Sayın {} zamlı maaşınız {} TL".format(ISIM, MAAS))
else:
    MAAS+= (MAAS*0.30)
    print("Sayın {} zamlı maaşınız {} TL".format(ISIM, MAAS))

# 2. Uygulama
KENAR1 = float(input("1. kenarı girin"))
KENAR2 = float(input("2. kenarı girin"))
KENAR3 = float(input("3. kenarı girin"))


if KENAR1 == KENAR2 and KENAR1 == KENAR3 and KENAR2 == KENAR3 :
    print("Bu üçgen eşkenar üçgendir")
elif (KENAR1 == KENAR2 and KENAR1!= KENAR3) or (KENAR1 == KENAR3 and KENAR1!= KENAR2) or (KENAR2 == KENAR3 and KENAR2!= KENAR1):
    print("Bu üçgen ikizkenardır")
else:
    print("Bu üçgen çeşitkenar üçgendir")

