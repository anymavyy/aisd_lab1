# Вариант 15.
# Натуральные числа, расположенные в порядке возрастания.
# Для каждой такой последовательности минимальное число вывести прописью.
buffer = ''
element = ''
min_num = '0'
count = 0
check = 0
dict = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',
        9: 'девять'}
with open("input.txt", 'r') as f:
    buffer = f.readline(1)  # читаем первый блок
    if not buffer:
        print("Файл пустой")
    while buffer:
        while buffer.isdigit():  # проверка на цифру
            element += buffer  # если есть цифра, добавляем к числу
            buffer = f.readline(1)  # читаем следующий блок
        if len(element) > 0 and int(element) > int(min_num):  # проверяем на длину и больше ли число минимального
            if check == 0:  # если число ещё не выведено
                min_num = element
                print('Минимальное число последовательности:', end=' ')  # вывод минимального
                for j in range(len(min_num)): # вывод минимального числа прописью
                    for l in dict:
                        if str(l) == min_num[j]:
                            print(dict[l], end=' ')
                            break
                print('')
                check += 1  # минимальное уже выведено
            else:
                min_num = element
            count += 1
        elif len(element) > 0 and int(element) < int(min_num):  # проверяем на длину и меньше ли число минимального
            min_num = element
            print('Минимальное число последовательности:', end=' ')  # вывод минимального
            for j in range(len(min_num)):
                for l in dict:
                    if str(l) == min_num[j]:
                        print(dict[l], end=' ')
                        break
            print('')
        element = ''
        buffer = f.read(1)  # читаем следующий блок
if count == 0:  # если нет нужных чисел
    print("Чисел не найдено", end=" ")