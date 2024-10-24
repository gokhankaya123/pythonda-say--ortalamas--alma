a = []
b = int(input("kaç tane sayinin ortalmasını alcaksiniz:"))

for i in range(b):
    c =int(input("sayiyi giriniz:"))
    a.append(c)
    d = sum(a)


    ortalama = d/len(a)

    print(ortalama)