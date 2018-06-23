a = 1
b = 2
fibonacci = [a,b]

for i in range (4000000):

    a,b = b, a+b
    fibonacci.append(b)

print(sum(fibonacci))