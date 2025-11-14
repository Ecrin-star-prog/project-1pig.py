import random

def zar_at():
    return random.randint(1, 6)

def oyuncu_turu(oyuncu_adi, toplam_puan):
    tur_puani = 0
    while True:
        secim = input(f"{oyuncu_adi}, zar atmak için 'a', puanı kaydetmek için 'k' yaz: ").lower()
        if secim == 'a':
            zar = zar_at()
            print(f"{oyuncu_adi} zar attı: {zar}")
            if zar == 1:
                print("1 geldi! Bu turdaki puanlar sıfırlandı.")
                return toplam_puan
            else:
                tur_puani += zar
                print(f"Tur puanı: {tur_puani} | Toplam puan: {toplam_puan}")
        elif secim == 'k':
            toplam_puan += tur_puani
            print(f"{oyuncu_adi} puanını kaydetti. Yeni toplam: {toplam_puan}")
            return toplam_puan
        else:
            print("Geçersiz giriş. Lütfen 'a' ya da 'k' gir.")

def pig_oyunu():
    print("🎲 Pig Zar Oyununa Hoş Geldiniz! İlk 100 puana ulaşan kazanır.")
    oyuncu1 = input("1. oyuncunun adı: ")
    oyuncu2 = input("2. oyuncunun adı: ")
    puan1 = puan2 = 0

    while puan1 < 100 and puan2 < 100:
        print(f"\n--- {oyuncu1}'in sırası ---")
        puan1 = oyuncu_turu(oyuncu1, puan1)
        if puan1 >= 100:
            print(f"\n🎉 Tebrikler {oyuncu1}, oyunu kazandın!")
            break

        print(f"\n--- {oyuncu2}'nin sırası ---")
        puan2 = oyuncu_turu(oyuncu2, puan2)
        if puan2 >= 100:
            print(f"\n🎉 Tebrikler {oyuncu2}, oyunu kazandın!")
            break

if __name__ == "__main__":
    pig_oyunu()
