#2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

x1 = float(input('Введите координату x первой точки: '))
y1 = float(input('Введите координату y первой точки: '))
x2 = float(input('Введите координату x второй точки: '))
y2 = float(input('Введите координату y второй точки: '))

if x1 == x2 :
    print(f'x = {x1} ')
else :
    k = (y2 - y1)/(x2 - x1)
    b = y1 - (x1*y2-x1*y1)/(x2 - x1)
    print(f'y = {k}x + {b}')