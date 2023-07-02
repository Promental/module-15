
def num_order_reverse(n): # функция разворачивает порядок цифр в целой части числа
    # достаем только модуль целой части числа
    n = int(abs(n))
    # если целая часть равна 0, то цикл ниже будет пропущен, на этот случай заранее определяется переменная
    if n == 0:
        new_n = '0'
    else:
        new_n = ''
    # цикл отнимает из числа последнюю цифру и подставляет справа к новой строковой переменной
    while n > 0:
        new_n += str(n % 10)
        n //= 10
    new_n = float(new_n)
    return new_n

def num_mantisa_reverse(n): # функция разворачивает порядок цифр в мантисе
    # достаем только модуль числа
    n = abs(n)
    new_n = ''
    # т.к. ф-ция на каждой итерации цикла переводит сдвигает мантису на одну цифру в целую часть, подставляя
    # каждую новую цифру слева, то необходима переменная, которая будет считать порядок сдвига
    order = 0
    while n - int(n) > 0:
        # в расчете переменной используется округление до 8,
        # т.к. без данного ограничения погрешности приводят к некорректному расчету
        new_n = str(int(round((n - int(n)), 8) * 10)) + new_n
        n = n * 10
        order += 1
    new_n = float(new_n) * (10 ** (-order))
    return new_n

def num_sign(n): # функция определяет знак числа. Ее необходимость в том что, после разворота -0 становится 0
    if n < 0:
        sign = -1
    else:
        sign = 1
    return sign


n1 = float(input('Введите первое число: '))
n2 = float(input('Введите второе число: '))

num_order_reverse_1 = num_order_reverse(n1)
num_order_reverse_2 = num_order_reverse(n2)

num_mantisa_reverse_1 = num_mantisa_reverse(n1)
num_mantisa_reverse_2 = num_mantisa_reverse(n2)

num_sign_1 = num_sign(n1)
num_sign_2 = num_sign(n2)


n1_reverse = (num_order_reverse_1 + num_mantisa_reverse_1) * num_sign_1
n2_reverse = num_order_reverse_2 + num_mantisa_reverse_2 * num_sign_2
sum_n = round(n1_reverse + n2_reverse, 2)

print('Первое число наоборот:', n1_reverse)
print('Первое число наоборот:', n2_reverse)
print('Сумма:', sum_n)











