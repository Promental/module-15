import math
def coin_search():
  print('Введите координаты поиска монетки')
  x = float(input('Введите координату x: '))
  y = float(input('Введите координату y: '))
  r = float(input('Введите радиус: '))

  if math.sqrt(x ** 2 + y ** 2) <= r:
    print('Монетка где-то рядом')
  else:
    print('Монетки в области нет')


  print()
  coin_search()

coin_search()

