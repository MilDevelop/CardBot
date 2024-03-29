LEXICON_RU: dict[str, str] = {'yes_button': 'ДА!',
                              'no_button': 'НЕТ',
                              'cancel': 'Отменить',
                               '/start': 'Привет! Сыграем в карты?',
                               '/help': 'Перетасовать колоду /shuffle \n'
                                        'Взять карту /take\n'
                                        'моя статиcтика побед /stat \n',
                              '/card': 'я выбрал случайную карту',
                              '/broken': 'Бито!',
                              '/take': 'Беру!',
                              'step_bot': 'Мой ход!',
                              'step_yourself': 'Ваш ход!',
                              'no_echo': 'Это событие не поддерживается',
                              'start_game': 'Игра начинается прямо сейчас!',
                              'win': 'Вы победили, поздравляю!',
                              'lose': 'Ура! Я победил!',
                              'no_card': 'Нужно перетасовать колоду!',
                              'draw': 'Ничья',
                              'not_cmd': 'Я не понимать...'}

def simbol(name: str):
    list = ['❤️', '♠️', '♣️', '♦️']
    if name == 'HEARTS':
        return list[0]
    elif name == 'SPADES':
        return list[1]
    elif name == 'CLUBS':
        return list[2]
    elif name == 'DIAMONDS':
        return list[3]