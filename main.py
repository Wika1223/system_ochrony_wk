companies = [
    ["Securitas", "Warszawa"],
    ["Solid Security", "Kraków"],
    ["Konsalnet", "Poznań"],
    ["Juwentus", "Gdańsk"]
]

def read_data_company(company_data: list) -> None:
    for c in company_data:
        print(f'Firma ochroniarska {c[0]} z miejscowości {c[1]}.')
read_data_company(companies)