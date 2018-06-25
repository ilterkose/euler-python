sayı = int(input("Sayı giriniz:"))
carpanlar = []
a = 2

while (a <= sayı):
    while (sayı % a == 0):
        sayı = sayı / a
        carpanlar.append(a)
    a += 1


print(carpanlar)