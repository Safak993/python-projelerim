isim = input("\n(Robot): Resim çizmek için isminizi giriniz.")
if not isim.isalpha():
    print("(system):böyle bir isim yok.")
    exit()
else:
    print("\n(system):Resim çizmeye hazırlan")

resim = input(f"\n(Robot)Çizmek istediğin şeyi yaz(kalp,kılıç,balta,kedi)\n,({isim}):->")

if not resim.isalpha():
     print("böyle bir yazım  yok ")
elif resim.lower() == "kalp":
    print("  **   **")
    print(" ****** **")
    print("**********")
    print(" ********")
    print("  ******")
    print("   ****")
    print("    **")
elif resim.lower() == "kılıç":
   print(" ||")
   print(" |||")
   print(" |||")
   print(" ||||")
   print(" ||||")
   print("-------")
   print("  ***")
   print("  ***")
elif resim.lower() == "balta":
    print(" */***/")
    print(" */***/")
    print(" */***/")
    print(" *")
    print(" *")
    print(" *")
elif resim.lower() == "kedi":
    print("  /\\\\_/\\\\")
    print(" |<o  o>|")
    print(" |> * < |")
    print(" |*****|")
    print("|*******|")
    print(" |/\\_/\\|")
else:("Böyle bir resim yok")