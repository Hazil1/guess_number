# Импорт функции получения случайных чисел из модуля random
from random import randint

number = randint(1, 100)
print('Угадай число от 1 до 100')

while True:
    # Получаем число от пользователя и сохраняем его в переменную
    guess = int(input("Введите число: "))

    # Если число меньше загаданного
    if guess < number:
        print('Ваше число меньше того, что загадано.')

    # Если число больше загаданного
    elif guess > number:
        print('Ваше число больше того, что загадано.')
    
    # Если число угадано
    elif guess == number:
        break

print('Отличная интуиция! Вы угадали число :)')

