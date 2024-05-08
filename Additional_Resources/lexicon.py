LEXICON_RU: dict[str, str] = {'yes_button': 'ДА!',
                              'no_button': 'НЕТ',
                              'cancel': 'Отменить',
                               '/start': 'Привет! Сыграем в карты?',
                               '/help': '''• Еще раз приветствуем вас в нашей игре! \n
• Здесь вы можете показать свое мастерство в игре "Карты - Дурак" \n
В скором времени, здесь будут и другие увлекательные игры \n
Перечень команд для взаимодействия с ботом: \n
 - /start - начало работы с ботом \n
 - /help - помощь (а иначе как бы вы увидели это сообщение) \n
 - /stat - ваша статистика побед, очков, ваш банк монет \n
 - /hint - здесь вы можете заполучить подсказку \n
 Непосредственно игровые команды:\n 
  - /stop - сброс игры \n
  - /take - вы уже из последних сил отбиваетесь, и тут бот кидает вам решающую карту, и вы принимаете решение все забрать...😭 \n
  - /broken - Бито! (вам больше нечего подкидывать) \n 
  • Остались вопросы?  Переходите в телеграмм-сообщество нашей игры \n
  -> https://t.me/+u8mplqkFXm9mODMy \n
  • По сотрудничеству Пишите на этот телеграмм -> @Milimitary \n
''',
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

def ober_simbol(name: str):
    if name == '❤️':
        return 'HEARTS'
    elif name == '♠️':
        return 'SPADES'
    elif name == '♣️':
        return 'CLUBS'
    elif name == '♦️':
        return 'DIAMONDS'

