x = int(input("Ваедите сумму вклада "))
p = int(input("Введите процент "))
y = int(input("Вкедите сумму цели "))
year = 0
while x < y:
    x *= 1 + p / 100
    x = int(100 * x) / 100
    year += 1
print(year)
