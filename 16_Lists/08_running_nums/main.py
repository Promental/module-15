# Создание изначального списка

list_num = []
for i in range(int(input('Укажите кол-во элементов: '))):
    print('Введите значение', i + 1, 'элемента: ', end='')
    list_num.append(int(input()))

print()

lag = int(input('Сдвиг: '))

list_num_new = []

for j in range(len(list_num)):
    list_num_new.append(list_num[j - lag])

print('\nИзначальный список: ', list_num)
print('Сдвинутый список: ', list_num_new)
