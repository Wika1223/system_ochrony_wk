from system_lib.model import companies
from system_lib.controller import *

from system_lib.model import companies
from system_lib.controller import *

while True:
    print('0 - zakończ program')
    print('1 - wyświetl firmy ochroniarskie')
    print('2 - dodaj firmę ochroniarską')
    print('3 - usuń firmę ochroniarską')
    print('4 - zaaktualizuj dane firmy ')
    choose = input('wybierz opcję: ')

    if choose == '0':
        break
    if choose == '1':
        read_data_company(companies)
    if choose == '2':
        add_company(companies)
    if choose == '3':
        remove_company(companies)
    if choose == '4':
        update_company(companies)
