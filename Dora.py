def giris():
    print("🎀 Dora'nın Dünyası'na Hoş Geldin!")
    print("Dora, sihirli bir yolculuğa çıkmak üzere.")
    print("Onu ilerletebilmek için bazı Python görevlerini çözmen gerekiyor.\n")

def soru1():
    print("🚪 1. Kapı: Değişken Kapısı")
    print("Soru: Bir değişken tanımlamak için hangisi doğrudur?")
    print("a) değişken = 10")
    print("b) 10 = değişken")
    cevap = input("Cevabın (a/b): ").lower()

    if cevap == "a":
        print("✅ Doğru! Kapı açıldı, Dora ilerliyor...\n")
        return True
    else:
        print("❌ Yanlış. Tekrar dene!\n")
        return False

def baslat():
    giris()
    if soru1():
        print("🎉 Dora yoluna devam ediyor!")
    else:
        print("💡 Dora yardımına ihtiyaç duyuyor.")

baslat()