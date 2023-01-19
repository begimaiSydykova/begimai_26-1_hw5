from random import randint
from decouple import config

from casino import wins, loss

win_slot = randint(1, 31)
capital = config('MY_MONEY', cast=int)
win = 0
lost = 0

while 1:
    question = input('Желаете сделать ставку? ')
    if question == 'да':
        print('Выбирайте слот от 1 до 30 и ставьте ставку: ')
        user_slot = int(input('Slot: '))
        user_bet = int(input('Money: '))
        if user_slot <= 30 and user_bet <= capital:
            if win_slot == user_slot:
                capital += wins(user_bet)
                win += 1
                print(f'Слот на который Вы поставили оказался выигрышным, вы выиграли: {wins(user_bet)}$')
            else:
                capital = loss(user_bet, capital)
                lost += 1
                print(f'Вы проиграли. У выс отсталось еще {capital}$')
        elif user_slot >= 31:
            print('Вы можете поставить на слоты от 1 до 30')
        elif user_bet > capital:
            print('Вы не можете поставить больше чем у вас есть!')
    elif question == 'нет':
        print(f'Вы выиграли ставок: {win}.\n'
              f'Вы проиграли ставок: {lost}.\n'
              f'У вас осталось {capital}$')
        break
    else:
        print('Доступные команды: да или нет')
