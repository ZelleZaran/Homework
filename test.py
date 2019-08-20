#Простой калькулятор.
user_input = None
num1 = 0
num2 = 0

print('Инструкции к пользованию:')
print('Введите "сложить", что бы сложить два числа.')
print('Введите "вычесть", чтобы получить разность двух чисел.')
print('Введите "умножить", чтобы умножить одно число на другое.')
print('Введите "разделить", чтобы разделить одно число на другое.')
print('Введите "степень", чтобы возвести число в данную степень.')
print('Введите "выход", чтобы выйти из программы.')

while True:

    user_input = input('Какую операцию вы хотите произвести? ')
    print(user_input)

    if user_input == 'выход':
        break
    elif user_input == 'сложить':
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
        result = str(num1+num2)
        print('Ответ: '+result)

    elif user_input == 'вычесть':
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
        result = str(num1 - num2)
        print('Ответ: ' + result)

    elif user_input == 'умножить':
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
        result = str(num1 * num2)
        print('Ответ: ' + result)

    elif user_input == 'разделить':
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
        result = str(num1 / num2)
        print('Ответ: ' + result)

    elif user_input == 'степень':
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
        result = str(num1 ** num2)
        print('Ответ: ' + result)

    else:
        print('Неверный ввод.')








