""" 1 Задача """
ans = input('Идёт ли дождь? ').lower()
if ans == "yes":
    ans2 = input('Ветрено ли на улице? ').lower()
    if ans2 == "yes":
        print('Слишком ветрено для зонтика')
    else:
        print('Возьмите зонтик')
else:
    print('Наслаждайтесь днём')

""" 2 Задача """
name = input('Введите имя в нижнем регистре ').title()
surname = input('Введите фамилию в нижнем регистре ').title()
print(name + " " + surname)

""" 3 Задача """
st = input('Введите строку какого-нибудь стихотворения ')
print(len(st))
start = int(input("введите начальную позицию "))
end = int(input("введите конечную позицию "))
print(st[start:end])

""" 4 Задача """
name = input('Введите имя ')
if len(name) < 5:
    surname = input('Введите фамилию ')
    print((name + surname).upper())
else: print(name.lower())

""" 5 Задача """
num = int(input('Введите число больше 500 '))
print(round(num ** 0.5, 2))

""" 6 Задача """
fig = input('Веведите слово круг или треугольник или прямоугольник ')
if fig.lower() == 'круг':
    r = int(input('Введите радиус '))
    from math import pi
    print(pi * r ** 2)
elif fig.lower() == 'треугольник':
    a = int(input('Введите 1 сторону треугольника '))
    b = int(input('Введите 2 сторону треугольника '))
    c = int(input('Введите 3 сторону треугольника '))
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif fig.lower() == 'прямоугольник':
    a = int(input('Введите длину 1 стороны '))
    b = int(input('Введите длину 2 стороны '))
    print(a * b)
