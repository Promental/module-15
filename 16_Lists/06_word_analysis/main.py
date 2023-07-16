word = input('Введите слово: ')

cnt_unic_char = 0

chars = list(word)
len_word = len(chars)

for i in range(len_word):
    cnt_repeat = 0
    for j in range(len_word):
        if chars[i] == chars[j]:
            cnt_repeat += 1
    if cnt_repeat == 1:
        cnt_unic_char += 1

print('Кол-во уникальных букв', cnt_unic_char)