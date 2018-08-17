import getpass
import re


def get_password_strength(password):
    min_len = 4
    average_len = 7
    password_strength = 1 
    pattern_special_characters = r'\W'
    password_special_characters = re.search(pattern_special_characters, password)
    pattern_dig = r'[0-9]+'
    password_dig = re.search(pattern_dig, password)
    if len(password) <= min_len:
        password_strength += 1
        return password_strength
    elif len(password) <= average_len:
        password_strength += 2
        return password_strength
    else:
        password_strength += 3
    if bool(password_dig):
        password_strength += 2
    if bool(password_special_characters):
        password_strength += 2
    if not password.islower() and not password.isupper():
        password_strength += 2
    return password_strength


def print_password_strength(password_strength):
    short_password_strength = 2
    low_security_password_strength = 5
    aver_security_password_strehgth = 7
    if password_strength <= short_password_strength:
        print('{} - Слишком простой пароль'.format(password_strength))
    elif password_strength <= low_security_password_strength:
        print('{} - Слабая надежность паролья'. format(password_strength))
    elif password_strength <= aver_security_password_strehgth:
        print('{} - Средняя надежность паролья'.format(password_strength))
    else:
        print('{} - Высокая надежность пароля'.format(password_strength))


if __name__ == '__main__':
    password = getpass.getpass('Введите пароль')
    password_strength = get_password_strength(password)
    print_password_strength(password_strength)
