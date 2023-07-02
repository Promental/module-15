

def main():

    y1 = int(input('Введите первый год: '))
    y2 = int(input('Введите последний год: '))

    for i in range(y1, y2 + 1):
        y = str(i)
        for j in y:
            s = 0
            for k in y:
                if k == j:
                    s += 1
            if s == 3:
                print(i)
                break

while True:
    main()
