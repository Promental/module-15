n = int(input('Кол-во видеокарт: '))

models_list = []
new_models_list = []

# Заведение списка видеокарт
for i in range(1, n + 1):
    print(i, end=' ')
    model = int(input('Видеокарта: '))
    models_list.append(model)

# Выявление видеокарты с наибольшим номером
max_model = max(models_list)

# Исключение из списка видеокарты с наибольшим номером
for i in range(len(models_list)):
    if models_list[i] != max_model:
        new_models_list.append(models_list[i])

print('Старый список видеокарт: [', ' '.join(str(x) for x in models_list), ']')

print('Новый список видеокарт: [', ' '.join(str(x) for x in new_models_list), ']')
