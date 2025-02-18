
# 1. Hello, World!
print("Hello, World!")

# 2. Kullanıcıdan ad alıp mesaj veren program
isim = input("Adınız nedir? ")
print(f"Merhaba, {isim}!")

# 3. Farklı veri tiplerinde değişkenler tanımlama ve işlemler
metin = "Python Öğreniyorum"
tamsayi = 10
ondalik = 3.14
dogru_mu = True

print(metin.upper())
print(tamsayi + 5)
print(ondalik * 2)
print(not dogru_mu)

# 4. Kullanıcıdan iki sayı alıp işlemler yapan program
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

print(f"Toplam: {sayi1 + sayi2}")
print(f"Fark: {sayi1 - sayi2}")
print(f"Çarpım: {sayi1 * sayi2}")

# 5. Değişken türlerini dönüştürme
tamsayi = 42
ondalik = float(tamsayi)
metin = str(tamsayi)

print(ondalik)
print(metin)

# 6. Kullanıcıdan cümle alıp büyük harfle yazdırma
cumle = input("Bir cümle girin: ")
print(cumle.upper())

# 7. Liste işlemleri
meyveler = ["Elma", "Armut", "Muz"]
meyveler.append("Çilek")
meyveler.remove("Armut")

print(meyveler)

# 8. Kullanıcıdan yaş alıp mesaj veren program
yas = int(input("Yaşınızı girin: "))

if yas > 18:
    print("18 yaşından büyüksünüz.")
else:
    print("18 yaşından küçüksünüz.")

# 9. Sayı tahmin oyunu
import random
dogru_sayi = random.randint(1, 10)
tahmin = int(input("1 ile 10 arasında bir sayı tahmin edin: "))

if tahmin == dogru_sayi:
    print("Tebrikler, doğru tahmin!")
else:
    print(f"Yanlış tahmin! Doğru sayı {dogru_sayi} idi.")

# 10. Gemi bulma oyunu
tahta = [["O" for _ in range(5)] for _ in range(5)]
gemi_satir = random.randint(0, 4)
gemi_sutun = random.randint(0, 4)

tahmin_hakki = 5
while tahmin_hakki > 0:
    print("\n".join([" ".join(satir) for satir in tahta]))
    print(f"Kalan tahmin hakkı: {tahmin_hakki}")

    tahmin_satir = int(input("Satır (0-4): "))
    tahmin_sutun = int(input("Sütun (0-4): "))

    if tahmin_satir == gemi_satir and tahmin_sutun == gemi_sutun:
        print("Tebrikler, gemiyi buldunuz!")
        break
    else:
        print("Yanlış tahmin!")
        tahta[tahmin_satir][tahmin_sutun] = "X"
        tahmin_hakki -= 1

if tahmin_hakki == 0:
    print(f"Oyun bitti! Gemi ({gemi_satir}, {gemi_sutun}) konumundaydı.")
