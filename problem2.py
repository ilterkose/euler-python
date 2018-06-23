a = 0
b = 1

fibonacci = [a,b]

while a < 4000000:
    print(a)
    a, b = b, a+b
    if  (b % 2) == 0:
        fibonacci.append(b)

print(sum(fibonacci))


a = 0
b = 1
toplam = 0
fibonacci = [a,b]

while a < 4000000:
    print(a)
    a, b = b, a+b
    if  (b % 2) == 0:
        toplam += b

print((toplam))


