print("hoşgeldiniz uygulamaya girmek için bilgilerinizi yaziniz.")
isim = input("İsminiz nedir?")

if not isim.isalpha():
    print("böyle bir isim yok")
    exit()
else:
    print("güzel isim")
    
    yaş = input("yaşınızı giriniz(Uygulama şüpheli içerikler içeriyor olabilir yaşınızı girmekten çekinmeyin)")
if not yaş.isdigit:
    print("böyle bir yaş yok")
    exit()
else:
    yaş = int(yaş)
    if yaş > 17:
        print("Güzel yaşınız tutuyor")
    else:
        print("malesef yaşınız tutmuyor")
        exit()
        
adres = input("lütfen ilçenizi yazınız")

maaş = input("günlük kaç para alacaksınız? yazınız(sayı ile!)")
if not maaş.isdigit:
    print("böyle bir maaş sayısı yok")
    exit()
else:
    maaş = int(maaş)
    if maaş < 30000:
        print("Uygun maaş")
    else:
        print("dengesiz pahalı maaş olmaz")
        exit()
ulaşım = input("size ulaşmamız için telefon numaranızı girin(sayı ile)")
if not ulaşım.isdigit:
    print("böyle bir numara yok")
    exit()
else:
     print("#########Kişini bilgileri#########")
     print("İsmi = ",isim)
     print("Yaşı = ",yaş)
     print("adresi = ",adres)
     print("maaşı(kazancı) = ",maaş)
     print("telefon numarası = ",ulaşım)
        

