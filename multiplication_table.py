from time import process_time

input_first = input ('Хотите посмотреть на таблицу умножения? Да/Нет - ')
if input_first == 'Да' or input_first == 'да':
    input_second = int(input ('''С 1 до 10 - напиши 1
C 11 До 20 - нвпиши 2
 '''))
    if input_second == 1:
        for i in range(1, 11):
            for j in range(1, 11):
                print(f'{i} x {j} = {i * j}')
    elif input_second == 2:
        for o in range(11, 21):
            for k in range(11, 21):
                print(f'{o} x {k} = {o * k}')
    else:
        print('А зачем тебе другие таблицы?')
else:
    print('На нет и суда нет!')
