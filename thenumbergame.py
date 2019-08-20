#Тема 3. Практикум «Угадай число».
#1. В этой игре человек загадывает число, а компьютер пытается его угадать.
#В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги. Компьютер начинает его отгадывать предлагая игроку варианты чисел.
#Если компьютер угадал число, игрок выбирает “победа”. Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”.
#Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”. Игра продолжается до тех пор пока компьютер не отгадает число.





attempt = 0
levels = {1: 3, 2: 5, 3: 7}
player_name = None
x=1
y=100
user_direction = None
guess_number = 0

i_need_your_name = input(' Ваше имя: ')
print(i_need_your_name)

print(f'Здравствуйте, {i_need_your_name}. Добро пожаловать в игру "The number game"!')
print('Вот ее правила:')
print('Вы загадываете число от 1 до 100, а компьютер угадывает. ')
print('Есть 1, 2, 3 уровня сложности по колличеству попыток.')
print('После каждой попытки Вы даете подсказку больше число, чем загаданное, или меньше.')

print('Начинаем игру!')


level_dif = int(input(f'{i_need_your_name}, выберете, пожалуйста, уровень сложности. 1, 2 или 3? '))
print(level_dif)
level_chs = levels[level_dif]




while user_direction != '=':

    attempt += 1

    if attempt > level_chs:
        print(f'Ай-яй-яй! Я проиграл. В этот раз победа за {i_need_your_name}!')
        break

    print(f'Попытка номер {attempt}')

    guess_number = (x + y) // 2
    print(guess_number)
    user_direction = str(input('Это число =, < или >? '))
    print(user_direction)

    if user_direction == '<':
        y = guess_number - 1
    elif user_direction == '>':
        x = guess_number + 1
    elif user_direction == '=':
        print('Ура! В этот раз победил компьютер.')
        break
    else:
        print('Вы ввели что-то неверно. Пожалуйста используйте только следующие символы: ">""<" или "="')





#Дописать выход из ошибочного ввода разного типа. Дописать возможность покинуть игру.



