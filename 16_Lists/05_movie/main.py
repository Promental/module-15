films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favour = []  # инициализация списка избранных фильмов
title = input('Введите название фильма: ')
print()

while title != 'end':
    # блок для определения есть ли фильм в списке избранных
    status_search = 0
    for i in favour:
        if i == title:
            status_search = 1
            print('Этот фильм уже содержится в Избранном')
            break

    # блок для добавления в избранное
    if status_search == 0:
        for j in films:
            if j == title:
                favour.append(title)
                print('Фильм добавлен в Избранное')
                status_search = 2
                break
        if status_search == 0:
            print('Указанного фильма не найдено')
    title = input('\nВведите название фильма: ')
