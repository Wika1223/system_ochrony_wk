from system_lib.model import companies
from system_lib.controller import *

from system_lib.model import companies
from system_lib.controller import *

while True:
    print('0 - zakończ program')
    print('1 - wyświetl firmy ochroniarskie')
    choose = input('wybierz opcję: ')

    if choose == '0':
        break
    if choose == '1':
        read_data_company(companies)
