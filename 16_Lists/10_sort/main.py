# Создание изначального списка
list_num = []
for i in range(int(input('Укажите кол-во элементов: '))):
    print('Введите значение', i + 1, 'элемента: ', end='')
    list_num.append(int(input()))

print('\nИзначальный список: ', list_num)

len_list_num = len(list_num)

# Оптимизированная пузырьковая сортировка
for i in range(len_list_num):
    for j in range(1, len_list_num - i):
        if list_num[j - 1] > list_num[j]:
            list_num[j - 1], list_num[j] = list_num[j], list_num[j - 1]

print('\nОтсортированный список: ', list_num)