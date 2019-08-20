number = 0

while True:

    number = int(input('Введите число: '))

    print(number)

    if 0 <= number <= 10:
        print(number ** 2)
        break

    elif number < 0 or number > 10:

        print('Неверный ввод. Пожалуйста, введите целое число от одного до десяти.')




