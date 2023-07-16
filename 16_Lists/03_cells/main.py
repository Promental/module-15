n = int(input('Кол-во клеток: '))

cell_list = []
not_allow = []

for i in range(n):
    print('Эффективность', i + 1, 'клетки: ', end='')
    eff_cell = int(input())
    cell_list.append(eff_cell)
    if cell_list[i] < i + 1:
        not_allow.append(eff_cell)

print('Неподходящие значения:', not_allow)