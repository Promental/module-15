import random

n = int(input('Кол-во контейнеров: '))
list_weights = []

# Флаг автоматической генерации невозрастающего списка весов контейнеров
flg_auto = input('Введите "y", если хотите сгенерировать список весов контейнеров автоматически: ')
print()

if flg_auto == 'y':
    max_wt = 200
    for i in range(n):
        if max_wt > 2:
            wt = random.randrange(max_wt // 2, max_wt + 1)
            max_wt = wt
        else:
            wt = 1
        print('Вес контейнера:', wt)
        list_weights.append(wt)
else:
    for i in range(n):
        wt = int(input('Введите вес контейнера: '))
        list_weights.append(wt)

new_wt = int(input('\nВведите вес нового контейнера: '))
list_weights_new = []  # Инициация нового списка весов контейнеров

num_insert = 1  # Инициация переменной отвечающей за порядковый номер нового контейнера в новом списке

if new_wt > list_weights[0]:  # Если новый контейнер тяжелее всех остальных
    list_weights_new.append(new_wt)
    list_weights_new.extend(list_weights)
elif new_wt <= list_weights[n - 1]:  # Если новый контейнер легче всех остальных или его вес равен наименьшему из списка
    num_insert = n + 1
    list_weights_new.extend(list_weights)
    list_weights_new.append(new_wt)
else:  # Если вес нового контейнера попадает в диапазон весов старых контейнеров
    # Цикл добавления весов из старого списка в новый, ДО значения когда вес очередного контейнера станет меньше нового
    for j in range(n):
        num_insert = j + 1
        if list_weights[j] >= new_wt:
            list_weights_new.append(list_weights[j])
        else:  # Добавление нового веса в список
            list_weights_new.append(new_wt)
            break
    for k in range(num_insert - 1, n):  # Новый цикл, который переносит оставшиеся веса из старого списка
        list_weights_new.append(list_weights[k])

print('\nНомер, куда встанет новый контейнер:', num_insert)

print('\n', list_weights_new)
