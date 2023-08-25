START_CMD = "start"
PLAY_CMD = "play"
TURN_CMD = "turn"
HELP_CMD = "help"

START = "Приветствую, введите \"/help\" для ознакомления с правилами"
ATTEMPTS = 12
LENPASSWORD = 4
MOREATTEMPTS = "Слишком много попыток"
ONLYNUM = "Можно вводить только цифры"
ONLYLENNUM = f"Можно вводить только {LENPASSWORD} цифры"
WIN = "Вы угадали пароль."
HELPRULES = "Правила игры: пароль состоит из четырёх цифр, при введении пароля будет показываться: сколько цифр Вы угадали,сколько из них стоят на правильных позициях." \
       f" У Вас есть {ATTEMPTS} попыток. Для начала игры введите \"/play\" и в следующем сообщении \"/turn 1234\""
INPUTRASSWORD = "Введите пароль: "
HELPTURN = "Введите \"/turn 1234\""
HELPSTART = "Введите /play"

def coincidences(b):
    return f'\n\nОбщее число совпавших цифр: {b}\n'
def coincidencesposicion(i):
    return f'Цифра совпала на позиции: {i + 1}'

