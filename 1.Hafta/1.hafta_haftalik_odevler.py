# 1. Hello, World!
# Bu program "Hello, World!" mesajını ekrana yazdırır.
print("Hello, World!")

# 2. Kullanıcıdan ad alıp mesaj veren program
# Kullanıcıdan adını girmesini ister ve bir selamlama mesajı gösterir.
isim = input("Adınız nedir? ")
print(f"Merhaba, {isim}!")

# 3. Farklı veri tiplerinde değişkenler tanımlama ve işlemler
# String, tam sayı, ondalık sayı ve boolean değişkenlerle işlemler yapar.
metin = "Python Ogreniyorum"
tamsayi = 5
ondalik = 3,5
dogru_mu = True

print(metin.upper())  # Metni büyük harflere çevirir.
print(tamsayi + 5)    # Tam sayı ile toplama işlemi yapar.
print(ondalik * 2)    # Ondalık sayıyı iki ile çarpar.
print(not dogru_mu)   # Boolean değeri tersine çevirir.

# 4. Kullanıcıdan iki sayı alıp işlemler yapan program
# Kullanıcıdan iki sayı alır ve toplama, çıkarma, çarpma işlemleri yapar.
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

print(f"Toplam: {sayi1 + sayi2}")
print(f"Fark: {sayi1 - sayi2}")
print(f"Carpim: {sayi1 * sayi2}")

# 5. Değişken türlerini dönüştürme
# Tam sayıyı ondalığa ve stringe dönüştürür.
tamsayi = 42
ondalik = float(tamsayi)
metin = str(tamsayi)

print(ondalik)
print(metin)

# 6. Kullanıcıdan cümle alıp büyük harfle yazdırma
# Kullanıcının girdiği cümleyi büyük harflerle ekrana yazdırır.
cumle = input("Bir cümle girin: ")
print(cumle.upper())

# 7. Liste işlemleri
# Bir liste oluşturur, listeye eleman ekler ve çıkarır.
meyveler = ["Defter", "Kalem", "Silgi"]
meyveler.append("Çanta")  # Listeye çilek ekler.
meyveler.remove("Kalem")  # Listeden armut çıkarır.

print(meyveler)

# 8. Kullanıcıdan yaş alıp mesaj veren program
# Kullanıcının yaşını alır ve bir mesaj gösterir.
yas = int(input("Yasınızı girin: "))

if yas > 18:
    print("18 yaşından büyüksünüz.")
else:
    print("18 yaşından küçüksünüz.")

# 9. Sayı tahmin oyunu
# Rastgele bir sayı oluşturur ve kullanıcının bu sayıyı tahmin etmesini ister.
import random
dogru_sayi = random.randint(1, 10)
tahmin = int(input("1 ile 10 arasında bir sayı tahmin edin: "))

if tahmin == dogru_sayi:
    print("Tebrikler, doğru tahmin!")
else:
    print(f"Yanlış tahmin! Doğru sayı {dogru_sayi} idi.")

# 10. Gemi bulma oyunu
import random

tahta = [["O"] * 5 for _ in range(5)]  # 5x5 oyun tahtası oluştur

# Geminin gizli olduğu rastgele bir konum seç
gemi_satir = random.randint(0, 4)  # 0 ile 4 arasında rastgele bir satır
gemi_sutun = random.randint(0, 4)  # 0 ile 4 arasında rastgele bir sütun

tahmin_hakki = 5  # Oyuncunun 5 tahmin hakkı var

while tahmin_hakki > 0:
    # Tahtayı ekrana yazdır
    for satir in tahta:
        print(" ".join(satir))  # Her satırı ekrana yazdır
    
    print(f"Kalan tahmin hakkı: {tahmin_hakki}")  # Kullanıcıya kalan hakkını göster

    # Kullanıcıdan satır ve sütun al
    tahmin_satir = int(input("Satır girin (0-4): "))
    tahmin_sutun = int(input("Sütun girin (0-4): "))

    if tahmin_satir == gemi_satir and tahmin_sutun == gemi_sutun:       # Eğer tahmin doğruysa
        print("Tebrikler, gemiyi buldunuz!")
        break  # Döngüden çık
    
    else:
        print("Yanlış tahmin!")
        tahta[tahmin_satir][tahmin_sutun] = "X"  # Yanlış tahmin yapılan yeri işaretle
        tahmin_hakki -= 1  # Kullanıcının hakkını bir azalt

if tahmin_hakki == 0: # Eğer tahmin hakkı biterse
    print(f"Oyun bitti! Gemi şurada saklıydı: ({gemi_satir}, {gemi_sutun})")

