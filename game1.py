#Попытка сделать задание в виде игры. Много косяков, но все-таки прилагаю.



def battle(person1, person2):
    player = {'name': person1, 'health': 100, 'damage': 50, 'armor': 1.2}
    enemy = {'name': person2, 'health': 300, 'damage': 15, 'armor': 1.4}

    def armor(pers1, pers2):
            strike = pers1 / pers2
            return int(strike)





    count = 0
    strike = None

    while True:

        count += 1
        print(f'Round {count}')

        print('*' * 100)

        print(f"It's a {player.get('name')}'s turn  to strike")

        strike = armor(player.get('damage'), enemy.get('armor'))
        strike = enemy.get('health') - strike
        enemy['health'] = strike

        print(
            f"{player.get('name')}'s health is {player.get('health')} and {enemy.get('name')}'s health is {enemy.get('health')} ")

        print(f"It's a {enemy.get('name')}'s turn  to strike")

        strike = armor(enemy.get('damage'), player.get('armor'))

        strike = player.get('health') - strike
        player['health'] = strike

        print(f"{player['name']}'s health is {player['health']} and {enemy['name']}'s health is {enemy['health']} ")

        if enemy['health'] <= 0 or player['health'] <= 0:
            return 'The battle is over!'



print(battle('Phobos', 'Doomguy'))