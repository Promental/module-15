list_char = list(input('Введите слово: '))

flg = 0  # Флаг, что слово НЕ является палиндромом

for i in range(len(list_char) // 2):
    if list_char[i] != list_char[-i - 1]:
        flg = 1
        break

if flg == 0:
  print('\nСлово является палиндромом')
else:
  print('\nСлово НЕ является палиндромом')