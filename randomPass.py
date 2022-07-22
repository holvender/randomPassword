from colorama import Fore, Back, Style
import random
import string
from colorama import init
init()


randLetter = string.ascii_letters


def r_str():
    return str(random.choice(randLetter))


def r_int():
    return str(random.randrange(0, 9))


randomSign = [r_str, r_int]
print(Fore.GREEN)
passLength = ''
save_file = input('Напишите путь для сохранения файла либо путь до существующего файла: ')
site = input('Для чего данные: ')
mail_login = input('Почта или Логин: ')

i = 0
genPass = ''


def pass_type_request():
    global passLength

    pass_type = input('Вам нужен случайный пароль? [yes]/[no]').lower()

    if pass_type == 'yes' or pass_type == 'ye' or pass_type == 'y' or \
            pass_type == 'да' or pass_type == 'д' or pass_type == 'da' or pass_type == 'd':

        passLength = int(input('Сколько символов должно быть в пароле: '))
        pass_gen()
        f = open(save_file, 'a')
        f.write(f"# {site}\n")
        f.write(f"mail/login: {mail_login}\n")
        f.write(f"password: {genPass}\n\n")
        print(Fore.YELLOW)
        print(f"\nВаш пароль: {genPass}\n")
        print(f"\nВаши данные сохранены!\n")

    elif pass_type == 'no' or pass_type == 'n' or pass_type == 'nah' or pass_type == 'nope' or \
            pass_type == 'нет' or pass_type == 'не' or pass_type == 'н' or pass_type == 'неа':

        password = input('Введите пароль для записи: ')
        f = open(save_file, 'a')
        f.write(f"# {site}\n")
        f.write(f"mail/login: {mail_login}\n")
        f.write(f"password: {password}\n\n")
        print(Fore.YELLOW)
        print(f"\nВаши данные сохранены!\n")


def pass_gen():
    global genPass
    global i
    while int(passLength) > len(genPass):
        genPass += random.choice(randomSign)()
        i += 1


pass_type_request()


print(Fore.CYAN)
input('Нажмите ENTER, чтобы завершить.')
