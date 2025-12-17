#Gizli hazine bulma oyunu
#Not: 👋Yaptığım ilk def time sleep ve ençok elif olan bir projem oyüzden ön yargılı olmayınız🙏
#Bol şans
import random
import time
isim = input("\n(Sistem):Oyunu başlatmak için ismini gir.\n(Kullanıcı):->")
if not isim.isalpha():#İsim harflimi kontrol
    print("böyle isim yok")
    exit()
else:
    print("(Sistem):Oyun başlıyor...")
time.sleep(1.5)#Sanki oyun yükleniyormuş hissi
print("(Sistem):Oyun başlıyor...")
time.sleep(0.5)
print("(sistem):Oyun başladı")
def harita_ciz(satir, sutun):
    if satir == 0 and sutun == 0:
        print("X * *\n* * *\n* * *")
    elif satir == 0 and sutun == 1:
        print("* X *\n* * *\n* * *")
    elif satir == 0 and sutun == 2:
        print("* * X\n* * *\n* * *")
    elif satir == 1 and sutun == 0:
        print("* * *\nX * *\n* * *")
    elif satir == 1 and sutun == 1:
        print("* * *\n* X *\n* * *")
    elif satir == 1 and sutun == 2:
        print("* * *\n* * X\n* * *")
    elif satir == 2 and sutun == 0:
        print("* * *\n* * *\nX * *")
    elif satir == 2 and sutun == 1:
        print("* * *\n* * *\n* X *")
    elif satir == 2 and sutun == 2:
        print("* * *\n* * *\n* * X")
sutun = 1
satir = 1
sayac = 0
hazine_satir = random.randint(0,2)
hazine_sutun = random.randint(0,2)
while hazine_satir == 1 and hazine_sutun == 1:
    hazine_satir = random.randint(0, 2)
    hazine_sutun = random.randint(0, 2)
print("\nHarita")
harita_ciz(satir, sutun)
while True:
    hareket = input(f"\n(Sistem)W/A/S/D ile hareket |Q ile durdur\n({isim}):->").upper()

    if hareket == "W" and satir > 0:
        satir -=1
        sayac += 1
    elif hareket == "S" and satir < 2:
        satir +=1
        sayac += 1
    elif hareket == "A" and sutun > 0:
        sutun -=1
        sayac += 1
    elif hareket == "D" and sutun < 2:
        sutun +=1
        sayac += 1

    elif hareket == "Q":
        print("(Sistem):Oyundan Çıkılıyor...")
        time.sleep(1.5)
        print("(Sistem):Oyundan Çıkılıyor...")
        time.sleep(0.5)
        print("(Sistem):Oyundan başarıyla çıkıldı.")
        break
    else:
        print("\n(Sistem):Böyle bir hareket tuşu yok.")
        break
    print("\nHarita")
    harita_ciz(satir, sutun)
    print(f"(Sistem):Hareket sayısı:{sayac} ")
    if satir == hazine_satir and sutun == hazine_sutun:
        print("\n🎁 🎁 🎁\n🎁 🎁 🎁\n🎁 🎁 🎁")
        print("\n(System):Gizli Hazineyi buldun 🎉")
        print(f"\n(System):Tam olarak{sayac}Denemede buldun🎉")
        break
    if sayac == 4:#4 Hakkın var biterse Kaybedersin
        print("\n(Sistem):Hakkınız bitti Oyunu kaybettin😒")
        break
