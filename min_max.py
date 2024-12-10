n_2 = list(input("Введите число: "))
while True:
    n_2_add = input("Введите число или стоп: ")
    if n_2_add == "Стоп" or n_2_add == "стоп":
        break
    else:
        n_2.append(n_2_add)
n_max = len(n_2) - 2
print("Число", sorted(n_2[n_max]), "меньше максимального из введенных вами чисел")