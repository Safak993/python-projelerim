#Not ### 19.12.2025 Yaptığım en büyük projedir(Yeniyim lütfen ön yargılı olmayınız🎈)
#👋Selam önceki Gizli hazineyi bul projemin bir güncellemesi
#İyi eğlenceler!😊
import random
import time

print("(Safak993):Hey selam👋")
time.sleep(1.5)
print("(Safak993):Bu oyunu yapan Safak993 bilgine🎈.")
time.sleep(1)
print("(Safak993):Sadece 20 Hakkın var Bol şans iyi eğlenceler😊")

isim = input("\n(Sistem):Oyuna başlamak için isminizi giriniz.\n(Kullanıcı):->")
if not isim.isalpha():
    print("\n(Sistem):Böyle bir isim yok(Doğru giriniz.)")
    exit()
else:
    print("\n(Sistem):Oyun Hazırlanıyor...")
time.sleep(1.5)
print("\n(Sistem):Oyun kodları yazılıyor...")
time.sleep(1)
print("(Sistem):Oyun başlıyor")
def harita_ciz(satir, sutun):
    if satir == 0 and sutun == 0:
        print("\nX * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 0 and sutun == 1:
        print("\n* X * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 0 and sutun == 2:
        print("\n* * X * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 0 and sutun == 3:
        print("\n* * * X * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 0 and sutun == 4:
        print("\n* * * * X * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 0 and sutun == 5:
        print("\n* * * * * X * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 0 and sutun == 6:
        print("\n* * * * * * X *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 0 and sutun == 7:
        print("\n* * * * * * * X\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 1 and sutun == 0:
        print("\n* * * * * * * *\nX * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 1 and sutun == 1:
        print("\n* * * * * * * *\n* X * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 1 and sutun == 2:
        print("\n* * * * * * * *\n* * X * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 1 and sutun == 3:
        print("\n* * * * * * * *\n* * * X * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 1 and sutun == 4:
        print("\n* * * * * * * *\n* * * * X * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 1 and sutun == 5:
        print("\n* * * * * * * *\n* * * * * X * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 1 and sutun == 6:
        print("\n* * * * * * * *\n* * * * * * X *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 1 and sutun == 7:
        print("\n* * * * * * * *\n* * * * * * * X\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 2 and sutun == 0:
        print("\n* * * * * * * *\n* * * * * * * *\nX * * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 2 and sutun == 1:
        print("\n* * * * * * * *\n* * * * * * * *\n* X * * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 2 and sutun == 2:
        print("\n* * * * * * * *\n* * * * * * * *\n* * X * * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 2 and sutun == 3:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * X * * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 2 and sutun == 4:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * X * * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 2 and sutun == 5:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * X * *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 2 and sutun == 6:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * X *\n* * * * * * * *\n* * * * * * * *")
    elif satir == 2 and sutun == 7:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * X\n* * * * * * * *\n* * * * * * * *")
    elif satir == 3 and sutun == 0:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\nX * * * * * * *\n* * * * * * * *")
    elif satir == 3 and sutun == 1:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* X * * * * * *\n* * * * * * * *")
    elif satir == 3 and sutun == 2:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * X * * * * *\n* * * * * * * *")
    elif satir == 3 and sutun == 3:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * X * * * *\n* * * * * * * *")
    elif satir == 3 and sutun == 4:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * X * * *\n* * * * * * * *")
    elif satir == 3 and sutun == 5:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * X * *\n* * * * * * * *")
    elif satir == 3 and sutun == 6:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * X *\n* * * * * * * *")
    elif satir == 3 and sutun == 7:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * X\n* * * * * * * *")
    elif satir == 4 and sutun == 0:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\nX * * * * * * *")
    elif satir == 4 and sutun == 1:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* X * * * * * *")
    elif satir == 4 and sutun == 2:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * X * * * * *")
    elif satir == 4 and sutun == 3:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * X * * * *")
    elif satir == 4 and sutun == 4:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * X * * *")
    elif satir == 4 and sutun == 5:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * X * *")
    elif satir == 4 and sutun == 6:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * X *")
    elif satir == 4 and sutun == 7:
        print("\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * *\n* * * * * * * X")

satir = 2
sutun = 4
sayac = 0
hazine_satir = random.randint(0,4)
hazine_sutun = random.randint(0,7)
while hazine_satir == 2 and hazine_sutun == 4:
    hazine_satir = random.randint(0,4)
    hazine_sutun = random.randint(0,7)
print("\nHarita")
harita_ciz(satir, sutun)
while True:
    hareket = input(f"(Sistem):W/A/S/D ile hareket et q ile kapat\n{isim}:->").upper()
    if hareket == "W" and satir > 0:
        satir -=1
        sayac +=1
    elif hareket == "S" and satir < 4:
        satir +=1
        sayac +=1
    elif hareket == "A" and sutun > 0:
        sutun -=1
        sayac +=1
    elif hareket == "D" and sutun < 7:
        sutun +=1
        sayac +=1
    elif hareket == "Q":
        print("(Sistem):Oyundan çıkılıyor...")
        time.sleep(1)
        print("(Sistem):Oyunun Kodları siliniyor...")
        time.sleep(1)
        print("(Sistem):Oyundan başarıyla çıkıldı!")
        break
    else:
        print("\n(Sistem):Böyle bir hareket tuşu yok/Böyle bir gidiş yeri yok.")
    print("\nHarita")
    harita_ciz(satir, sutun)
    print(f"Şuana kadar {sayac} kez denediniz.")
    if satir == hazine_satir and sutun == hazine_sutun:
        print("\n🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇\n🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇\n🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇\n🎇 🎇 🎇 🎇 🎇 🎇 🎇 🎇")
        print("(Sistem):Tebrikler! Oyunu kazandınız🎉🎉")
        print("(Sistem):Oyun kapatılıyor...")
        break
    if sayac == 20:
        print("Hakkınız bitti. Kaybettiniz🙄😐")
        break
#Oyunu sevdiyseniz lütfen star(yıldız bırakınız)
#By: Safak993(mirac2_2)








