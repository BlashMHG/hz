input_main = int(input("""Здравствуйте! выберите одну из программ:
1. Вычисление второго максимального числа из введенных вами
2. Задача древний шифр
3. Узнать конечную сумму вклада
Выберите цифру нужной программы:  
"""))
def maximum():
    n_2 = list(input("Введите число: "))
    while True:
        n_2_add = input("Введите число или стоп: ")
        if n_2_add == "Стоп" or n_2_add == "стоп":
            break
        else:
            n_2.append(n_2_add)
        
        n_max = len(n_2) - 2
    print("Число", sorted(n_2[n_max]), "меньше максимального из введенных вами чисел")

def key():
    input_ = int(input("Введрте число от 3 до 20 - "))
    if input_ < 3 or input_ > 20:
        print("""   Введенное число не подходит
   Пожалуйста, следуйте условиям ввода""")
    else:
        input_list = list(range(1, input_)) 
    answer = []
    for i in input_list:
        for j in input_list:
            i_IL = i  #IL = input list
            j_IL = j
            if i_IL >= j_IL:
                continue
            else:
                kratnost = input_ % (i_IL + j_IL)
                if kratnost == 0:
                    answer.append([i_IL, j_IL])
    print(*answer)
    
def bank():
    x = int(input("Ваедите сумму вклада "))
    p = int(input("Введите процент "))
    y = int(input("Вкедите сумму цели "))
    year = 0
    while x < y:
        x *= 1 + p / 100
        x = int(100 * x) / 100
        year += 1
    print("Через", year, "лет, сумма вклада достигнет", y)

if input_main == 3:
    bank()
elif input_main == 2:
    key()
elif input_main == 1:
    maximum()
else:
    print("Такой программы нет")
