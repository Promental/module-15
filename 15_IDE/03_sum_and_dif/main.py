n = int(input('Введите число: '))

def sum_digit(n):
  s = 0
  while n > 0:
    s += n % 10
    n //= 10
  return s

def cnt_digit(n):
  c = 0
  for i in str(n):
    c += 1
  return c

sum_d = sum_digit(n)
cnt_d = cnt_digit(n)
diff = sum_d - cnt_d

print('Сумма цифр:', sum_d)
print('Кол-во цифр в числе:', cnt_d)
print('Разность суммы и кол-ва цифр:', diff)

