def read_data_company(company_data: list) -> None:
    for c in company_data:
        print(f'Firma ochroniarska {c[0]} z miejscowości {c[1]}.')
companies = [
    ["Securitas", "Warszawa"],
    ["Solid Security", "Kraków"],
    ["Konsalnet", "Poznań"],
    ["Juwentus", "Gdańsk"]]
read_data_company(companies)

def add_company(company_data: list) -> None:
    name = input('Podaj nazwę firmy: ')
    location = input('Podaj lokalizację: ')
    company_data.append([name, location])

def remove_company(company_data: list) -> None:
    name = input('Podaj nazwę firmy do usunięcia: ')
    for c in company_data:
        if c[0] == name:
            company_data.remove(c)

def update_company(company_data: list) -> None:
    name = input('Podaj nazwe firmy do zmiany: ')
    for c in company_data:
        if c[0] == name:
            c[0] = input('Podaj nową nazwę firmy: ')
            c[1] = input('Podaj nową lokalizację: ')
