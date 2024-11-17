from multiprocessing.connection import answer_challenge

name = input("Введите ваше имя: ")
print("здравсвтвуйте, " .upper(), name)
print('Как ваши дела? Хорошо/Плохо')
answer = input()
if answer =='Хорошо':
    print('Ура! Это же просто замечатнльно')
if answer =='Плохо':
    print('Грустно( Попробуйте выпить кофе и высказаться близкому человеку!')
age = input('А в каком году вы родились? ')
year = 2024
now_age =  year - int(age)
if now_age <18:
    print('Извините, программа строго 18+')
if now_age>=18:
    print('Добро пожаловать в улуб Скуфов! Хе-хе')
