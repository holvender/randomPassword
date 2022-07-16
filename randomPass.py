import random
import string
from colorama import init
init()
from colorama import Fore, Back, Style


randLetter = string.ascii_letters


def r_str():
    return str(random.choice(randLetter))


def r_int():
    return str(random.randrange(0, 9))


randomSign = [r_str, r_int]
print(Fore.GREEN)
passLength = int(input('Сколько символов должно быть в пароле: '))

i = 0
genPass = ''

while passLength > int(len(genPass)):
    genPass += random.choice(randomSign)()
    i += 1

print(Fore.YELLOW)
print(f"\nВаш пароль: {genPass}\n")

print(Fore.CYAN)
input('Нажмите ENTER, чтобы завершить.')
