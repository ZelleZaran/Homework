name=input('Введите Ваше имя:')
surname=input('Введите Вашу фамилию:')
age=int(input('Укажите Ваш возраст:'))
weight=int(input('Укажите Ваш вес:'))
if age<30 and 50<weight<120:
    print(name, surname, ', Вы в отличной форме!')
elif age>30 and 50<weight<120:
    print (name, surname, ', уделите себе больше внимания.')
elif age<30 and weight<50:
    print(name, surname, ', Вам нужно лучше питаться.')
elif age>30 and (weight<50 or weight>120):
    print(name, surname, ', Вам нужно показаться врачу.')
elif age<30 and weight>120:
    print(name, surname, ', Вам следует сесть на диету.')
else:
    print(name, surname, ', Вы уникальны и неповторимы. У нас нет совета для Вас.')