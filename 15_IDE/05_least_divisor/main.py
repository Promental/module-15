

def main():
    # функция расчитывает наименьший делитель (>1) натурального числа N (>1)
    def min_divider(n):
        if n % 2 == 0:
            div = 2
        else:
            for i in range(3, n + 1, 2):
                if n % i == 0:
                    div = i
                    break
        return div


    min_div = min_divider(n)

    print('Наименьший делитель, отличный от единицы:', min_div)

while True:
    n = input('\nВведите число: ')
    if n.isnumeric():
        n = int(n)
        if n > 1:
          main()
        else:
            print('Введено некорректное значение. Попробуйте снова!')
    else:
        print('Введено некорректное значение. Попробуйте снова!')