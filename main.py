from tkinter import *
from tkinter import ttk
import tkintermapview
from system_lib.model import Firma, Klient, Pracownik, Wartownia

#BAZA
companies = [
    Firma("Solid Security", "Warszawa", "521-03-21-528", "ul. Postępu 17"),
    Firma("Konsalnet", "Kraków", "527-20-27-282", "ul. Kamińskiego 1"),
    Firma("Securitas", "Poznań", "522-23-40-331", "ul. Dąbrowskiego 79A")]

clients = [
    Klient("Jan", "Kowalski", "Wrocław", "Solid Security"),
    Klient("Anna", "Nowak", "Gdańsk", "Konsalnet"),
    Klient("Piotr", "Wiśniewski", "Szczecin", "Securitas")]

employees = [
    Pracownik("Marek", "Wójcik", "Warszawa", "Solid Security", "111-222-333"),
    Pracownik("Katarzyna", "Kamińska", "Kraków", "Konsalnet", "444-555-666"),
    Pracownik("Tomasz", "Lewandowski", "Poznań", "Securitas", "777-888-999")]

guardhouses = [
    Wartownia("Wartownia Północ", "Gdynia", "Konsalnet"),
    Wartownia("Wartownia Centrum", "Warszawa", "Solid Security")]

def zaktualizuj_listy_wyboru():
    nazwy_firm = [f.nazwa for f in companies]
    combobox_firma_klienta['values'] = nazwy_firm
    combobox_firma_pracownika['values'] = nazwy_firm
    combobox_firma_wartowni['values'] = nazwy_firm


# FUNKCJE
# FIRMY
def show_companies():
    listbox_firmy.delete(0, END)
    for idx, firma in enumerate(companies):
        listbox_firmy.insert(idx, firma.nazwa)

def add_company():
    new_company = Firma(nazwa=entry_nazwa_firmy.get(), lokalizacja=entry_lokalizacja_firmy.get(),
                        nip=entry_nip_firmy.get(), adres=entry_adres_firmy.get())
    companies.append(new_company)
    entry_nazwa_firmy.delete(0, END)
    entry_lokalizacja_firmy.delete(0, END)
    entry_nip_firmy.delete(0, END)
    entry_adres_firmy.delete(0, END)
    show_companies()
    zaktualizuj_listy_wyboru()
    filtruj_mape()

def remove_company():
    i = listbox_firmy.index(ACTIVE)
    companies.pop(i)
    show_companies()
    zaktualizuj_listy_wyboru()
    filtruj_mape()

def show_company_details():
    i = listbox_firmy.index(ACTIVE)
    label_det_firma_nazwa_val.config(text=companies[i].nazwa)
    label_det_firma_lok_val.config(text=companies[i].lokalizacja)
    label_det_firma_nip_val.config(text=companies[i].nip)
    label_det_firma_adres_val.config(text=companies[i].adres)
    if companies[i].coordinates:
        map_widget.set_position(companies[i].coordinates[0], companies[i].coordinates[1])
        map_widget.set_zoom(12)

def edit_company():
    i = listbox_firmy.index(ACTIVE)
    entry_nazwa_firmy.delete(0, END)
    entry_lokalizacja_firmy.delete(0, END)
    entry_nip_firmy.delete(0, END)
    entry_adres_firmy.delete(0, END)

    entry_nazwa_firmy.insert(0, companies[i].nazwa)
    entry_lokalizacja_firmy.insert(0, companies[i].lokalizacja)
    entry_nip_firmy.insert(0, companies[i].nip)
    entry_adres_firmy.insert(0, companies[i].adres)

    button_dodaj_firme.config(text="Zapisz zmiany", command=lambda: update_company(i))

def update_company(i):
    companies[i].nazwa = entry_nazwa_firmy.get()
    companies[i].lokalizacja = entry_lokalizacja_firmy.get()
    companies[i].nip = entry_nip_firmy.get()
    companies[i].adres = entry_adres_firmy.get()
    companies[i].coordinates = companies[i].get_coordinates()

    button_dodaj_firme.config(text="Dodaj firmę", command=add_company)
    entry_nazwa_firmy.delete(0, END)
    entry_lokalizacja_firmy.delete(0, END)
    entry_nip_firmy.delete(0, END)
    entry_adres_firmy.delete(0, END)
    show_companies()
    zaktualizuj_listy_wyboru()
    filtruj_mape()

# KLIENCI
def show_clients():
    listbox_klienci.delete(0, END)
    for idx, klient in enumerate(clients):
        listbox_klienci.insert(idx, f"{klient.imie} {klient.nazwisko}")

def add_client():
    new_client = Klient(
        imie=entry_imie_klienta.get(), nazwisko=entry_nazwisko_klienta.get(),
        lokalizacja=entry_lokalizacja_klienta.get(), przypisana_firma=combobox_firma_klienta.get()
    )
    clients.append(new_client)
    entry_imie_klienta.delete(0, END)
    entry_nazwisko_klienta.delete(0, END)
    entry_lokalizacja_klienta.delete(0, END)
    combobox_firma_klienta.set('')
    show_clients()
    filtruj_mape()

def remove_client():
    i = listbox_klienci.index(ACTIVE)
    clients.pop(i)
    show_clients()
    filtruj_mape()

def show_client_details():
    i = listbox_klienci.index(ACTIVE)
    label_det_klient_imie_val.config(text=clients[i].imie)
    label_det_klient_nazw_val.config(text=clients[i].nazwisko)
    label_det_klient_lok_val.config(text=clients[i].lokalizacja)
    label_det_klient_firma_val.config(text=clients[i].przypisana_firma)
    if clients[i].coordinates:
        map_widget.set_position(clients[i].coordinates[0], clients[i].coordinates[1])
        map_widget.set_zoom(12)

def edit_client():
    i = listbox_klienci.index(ACTIVE)
    entry_imie_klienta.delete(0, END)
    entry_nazwisko_klienta.delete(0, END)
    entry_lokalizacja_klienta.delete(0, END)
    combobox_firma_klienta.set('')

    entry_imie_klienta.insert(0, clients[i].imie)
    entry_nazwisko_klienta.insert(0, clients[i].nazwisko)
    entry_lokalizacja_klienta.insert(0, clients[i].lokalizacja)
    combobox_firma_klienta.set(clients[i].przypisana_firma)

    button_dodaj_klienta.config(text="Zapisz zmiany", command=lambda: update_client(i))

def update_client(i):
    clients[i].imie = entry_imie_klienta.get()
    clients[i].nazwisko = entry_nazwisko_klienta.get()
    clients[i].lokalizacja = entry_lokalizacja_klienta.get()
    clients[i].przypisana_firma = combobox_firma_klienta.get()
    clients[i].coordinates = clients[i].get_coordinates()

    button_dodaj_klienta.config(text="Dodaj klienta", command=add_client)
    entry_imie_klienta.delete(0, END)
    entry_nazwisko_klienta.delete(0, END)
    entry_lokalizacja_klienta.delete(0, END)
    combobox_firma_klienta.set('')
    show_clients()
    filtruj_mape()

# PRACOWNICY
def show_employees():
    listbox_pracownicy.delete(0, END)
    for idx, pracownik in enumerate(employees):
        listbox_pracownicy.insert(idx, f"{pracownik.imie} {pracownik.nazwisko}")

def add_employee():
    new_employee = Pracownik(
        imie=entry_imie_pracownika.get(), nazwisko=entry_nazwisko_pracownika.get(),
        telefon=entry_telefon_pracownika.get(), lokalizacja=entry_lokalizacja_pracownika.get(),
        przypisana_firma=combobox_firma_pracownika.get()
    )
    employees.append(new_employee)
    entry_imie_pracownika.delete(0, END)
    entry_nazwisko_pracownika.delete(0, END)
    entry_telefon_pracownika.delete(0, END)
    entry_lokalizacja_pracownika.delete(0, END)
    combobox_firma_pracownika.set('')
    show_employees()
    filtruj_mape()

def remove_employee():
    i = listbox_pracownicy.index(ACTIVE)
    employees.pop(i)
    show_employees()
    filtruj_mape()

def show_employee_details():
    i = listbox_pracownicy.index(ACTIVE)
    label_det_prac_imie_val.config(text=employees[i].imie)
    label_det_prac_nazw_val.config(text=employees[i].nazwisko)
    label_det_prac_tel_val.config(text=employees[i].telefon)
    label_det_prac_lok_val.config(text=employees[i].lokalizacja)
    label_det_prac_firma_val.config(text=employees[i].przypisana_firma)
    if employees[i].coordinates:
        map_widget.set_position(employees[i].coordinates[0], employees[i].coordinates[1])
        map_widget.set_zoom(12)

def edit_employee():
    i = listbox_pracownicy.index(ACTIVE)
    entry_imie_pracownika.delete(0, END)
    entry_nazwisko_pracownika.delete(0, END)
    entry_telefon_pracownika.delete(0, END)
    entry_lokalizacja_pracownika.delete(0, END)
    combobox_firma_pracownika.set('')

    entry_imie_pracownika.insert(0, employees[i].imie)
    entry_nazwisko_pracownika.insert(0, employees[i].nazwisko)
    entry_telefon_pracownika.insert(0, employees[i].telefon)
    entry_lokalizacja_pracownika.insert(0, employees[i].lokalizacja)
    combobox_firma_pracownika.set(employees[i].przypisana_firma)

    button_dodaj_pracownika.config(text="Zapisz zmiany", command=lambda: update_employee(i))

def update_employee(i):
    employees[i].imie = entry_imie_pracownika.get()
    employees[i].nazwisko = entry_nazwisko_pracownika.get()
    employees[i].telefon = entry_telefon_pracownika.get()
    employees[i].lokalizacja = entry_lokalizacja_pracownika.get()
    employees[i].przypisana_firma = combobox_firma_pracownika.get()
    employees[i].coordinates = employees[i].get_coordinates()

    button_dodaj_pracownika.config(text="Dodaj pracownika", command=add_employee)
    entry_imie_pracownika.delete(0, END)
    entry_nazwisko_pracownika.delete(0, END)
    entry_telefon_pracownika.delete(0, END)
    entry_lokalizacja_pracownika.delete(0, END)
    combobox_firma_pracownika.set('')
    show_employees()
    filtruj_mape()

# WARTOWNIE
def show_guardhouses():
    listbox_wartownie.delete(0, END)
    for idx, wartownia in enumerate(guardhouses):
        listbox_wartownie.insert(idx, wartownia.nazwa)

def add_guardhouse():
    new_guardhouse = Wartownia(nazwa=entry_nazwa_wartowni.get(),lokalizacja=entry_lokalizacja_wartowni.get(),
                               przypisana_firma=combobox_firma_wartowni.get())
    guardhouses.append(new_guardhouse)
    entry_nazwa_wartowni.delete(0, END)
    entry_lokalizacja_wartowni.delete(0, END)
    combobox_firma_wartowni.set('')
    show_guardhouses()
    filtruj_mape()

def remove_guardhouse():
    i = listbox_wartownie.index(ACTIVE)
    guardhouses.pop(i)
    show_guardhouses()
    filtruj_mape()

def show_guardhouse_details():
    i = listbox_wartownie.index(ACTIVE)
    label_det_wart_nazwa_val.config(text=guardhouses[i].nazwa)
    label_det_wart_lok_val.config(text=guardhouses[i].lokalizacja)
    label_det_wart_firma_val.config(text=guardhouses[i].przypisana_firma)
    if guardhouses[i].coordinates:
        map_widget.set_position(guardhouses[i].coordinates[0], guardhouses[i].coordinates[1])
        map_widget.set_zoom(12)

def edit_guardhouse():
    i = listbox_wartownie.index(ACTIVE)
    entry_nazwa_wartowni.delete(0, END)
    entry_lokalizacja_wartowni.delete(0, END)
    combobox_firma_wartowni.set('')

    entry_nazwa_wartowni.insert(0, guardhouses[i].nazwa)
    entry_lokalizacja_wartowni.insert(0, guardhouses[i].lokalizacja)
    combobox_firma_wartowni.set(guardhouses[i].przypisana_firma)

    button_dodaj_wartownie.config(text="Zapisz zmiany", command=lambda: update_guardhouse(i))

def update_guardhouse(i):
    guardhouses[i].nazwa = entry_nazwa_wartowni.get()
    guardhouses[i].lokalizacja = entry_lokalizacja_wartowni.get()
    guardhouses[i].przypisana_firma = combobox_firma_wartowni.get()
    guardhouses[i].coordinates = guardhouses[i].get_coordinates()

    button_dodaj_wartownie.config(text="Dodaj wartownię", command=add_guardhouse)
    entry_nazwa_wartowni.delete(0, END)
    entry_lokalizacja_wartowni.delete(0, END)
    combobox_firma_wartowni.set('')
    show_guardhouses()
    filtruj_mape()

root=Tk()
root.title("System Ochrony - WKL")
root.geometry("1100x850")

# MAPA
ramka_mapa = Frame(root)
ramka_mapa.pack(side=BOTTOM, pady=10)
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1050, height=400, corner_radius=4)
map_widget.set_zoom(6)
map_widget.set_position(52.23, 21.00)
map_widget.pack()

# ZAKŁADKI
notebook = ttk.Notebook(root)
notebook.pack(fill=BOTH, expand=True, pady=10)

tab_firmy = Frame(notebook)
tab_klienci = Frame(notebook)
tab_pracownicy = Frame(notebook)
tab_wartownie = Frame(notebook)

notebook.add(tab_firmy, text="FIRMY")
notebook.add(tab_klienci, text="KLIENCI")
notebook.add(tab_pracownicy, text="PRACOWNICY")
notebook.add(tab_wartownie, text="WARTOWNIE")

# FIRMY
# RAMKI
ramka_lista_firmy = Frame(tab_firmy)
ramka_formularz_firmy = Frame(tab_firmy)
ramka_szczegoly_firmy = Frame(tab_firmy)

ramka_lista_firmy.grid(row=0, column=0, padx=20, pady=10, sticky=N)
ramka_formularz_firmy.grid(row=0, column=1, padx=20, pady=10, sticky=N)
ramka_szczegoly_firmy.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky=W)

# Lista
Label(ramka_lista_firmy, text="Lista firm:").grid(row=0, column=0, sticky=W)
listbox_firmy = Listbox(ramka_lista_firmy, width=30)
listbox_firmy.grid(row=1, column=0, columnspan=3, pady=5)
Button(ramka_lista_firmy, text="Szczegóły", command=show_company_details).grid(row=2, column=0)
Button(ramka_lista_firmy, text="Usuń", command=remove_company).grid(row=2, column=1)
Button(ramka_lista_firmy, text="Edytuj", command=edit_company).grid(row=2, column=2)

# Formularz
Label(ramka_formularz_firmy, text="Formularz:").grid(row=0, column=0, columnspan=2, sticky=W)
Label(ramka_formularz_firmy, text="Nazwa:").grid(row=1, column=0, sticky=W)
Label(ramka_formularz_firmy, text="Lokalizacja:").grid(row=2, column=0, sticky=W)
Label(ramka_formularz_firmy, text="NIP:").grid(row=3, column=0, sticky=W)
Label(ramka_formularz_firmy, text="Adres:").grid(row=4, column=0, sticky=W)

entry_nazwa_firmy = Entry(ramka_formularz_firmy)
entry_lokalizacja_firmy = Entry(ramka_formularz_firmy)
entry_nip_firmy = Entry(ramka_formularz_firmy)
entry_adres_firmy = Entry(ramka_formularz_firmy)

entry_nazwa_firmy.grid(row=1, column=1)
entry_lokalizacja_firmy.grid(row=2, column=1)
entry_nip_firmy.grid(row=3, column=1)
entry_adres_firmy.grid(row=4, column=1)

button_dodaj_firme = Button(ramka_formularz_firmy, text="Dodaj firmę", command=add_company)
button_dodaj_firme.grid(row=5, column=0, columnspan=2, pady=10)

# Szczegóły
Label(ramka_szczegoly_firmy, text="Szczegóły firmy:").grid(row=0, column=0, sticky=W)
Label(ramka_szczegoly_firmy, text="Nazwa:").grid(row=1, column=0, sticky=W)
label_det_firma_nazwa_val = Label(ramka_szczegoly_firmy, text="...")
label_det_firma_nazwa_val.grid(row=1, column=1, sticky=W, padx=10)
Label(ramka_szczegoly_firmy, text="Lokalizacja:").grid(row=1, column=2, sticky=W)
label_det_firma_lok_val = Label(ramka_szczegoly_firmy, text="...")
label_det_firma_lok_val.grid(row=1, column=3, sticky=W, padx=10)
Label(ramka_szczegoly_firmy, text="NIP:").grid(row=1, column=4, sticky=W)
label_det_firma_nip_val = Label(ramka_szczegoly_firmy, text="...")
label_det_firma_nip_val.grid(row=1, column=5, sticky=W, padx=10)
Label(ramka_szczegoly_firmy, text="Adres:").grid(row=1, column=6, sticky=W)
label_det_firma_adres_val = Label(ramka_szczegoly_firmy, text="...")
label_det_firma_adres_val.grid(row=1, column=7, sticky=W, padx=10)

# KLIENCI
# RAMKI
ramka_lista_klienci = Frame(tab_klienci)
ramka_formularz_klienci = Frame(tab_klienci)
ramka_szczegoly_klienci = Frame(tab_klienci)

ramka_lista_klienci.grid(row=0, column=0, padx=20, pady=10, sticky=N)
ramka_formularz_klienci.grid(row=0, column=1, padx=20, pady=10, sticky=N)
ramka_szczegoly_klienci.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky=W)

# Lista
Label(ramka_lista_klienci, text="Lista klientów:").grid(row=0, column=0, sticky=W)
listbox_klienci = Listbox(ramka_lista_klienci, width=30)
listbox_klienci.grid(row=1, column=0, columnspan=3, pady=5)
Button(ramka_lista_klienci, text="Szczegóły", command=show_client_details).grid(row=2, column=0)
Button(ramka_lista_klienci, text="Usuń", command=remove_client).grid(row=2, column=1)
Button(ramka_lista_klienci, text="Edytuj", command=edit_client).grid(row=2, column=2)

# Formularz
Label(ramka_formularz_klienci, text="Formularz:").grid(row=0, column=0, columnspan=2, sticky=W)
Label(ramka_formularz_klienci, text="Imię:").grid(row=1, column=0, sticky=W)
Label(ramka_formularz_klienci, text="Nazwisko:").grid(row=2, column=0, sticky=W)
Label(ramka_formularz_klienci, text="Lokalizacja:").grid(row=3, column=0, sticky=W)
Label(ramka_formularz_klienci, text="Firma:").grid(row=4, column=0, sticky=W)

entry_imie_klienta = Entry(ramka_formularz_klienci)
entry_nazwisko_klienta = Entry(ramka_formularz_klienci)
entry_lokalizacja_klienta = Entry(ramka_formularz_klienci)
combobox_firma_klienta = ttk.Combobox(ramka_formularz_klienci, state='readonly')

entry_imie_klienta.grid(row=1, column=1)
entry_nazwisko_klienta.grid(row=2, column=1)
entry_lokalizacja_klienta.grid(row=3, column=1)
combobox_firma_klienta.grid(row=4, column=1)

button_dodaj_klienta = Button(ramka_formularz_klienci, text="Dodaj klienta", command=add_client)
button_dodaj_klienta.grid(row=5, column=0, columnspan=2, pady=10)

# Szczegóły
Label(ramka_szczegoly_klienci, text="Szczegóły klienta:").grid(row=0, column=0, sticky=W)
Label(ramka_szczegoly_klienci, text="Imię:").grid(row=1, column=0, sticky=W)
label_det_klient_imie_val = Label(ramka_szczegoly_klienci, text="...")
label_det_klient_imie_val.grid(row=1, column=1, sticky=W, padx=10)
Label(ramka_szczegoly_klienci, text="Nazwisko:").grid(row=1, column=2, sticky=W)
label_det_klient_nazw_val = Label(ramka_szczegoly_klienci, text="...")
label_det_klient_nazw_val.grid(row=1, column=3, sticky=W, padx=10)
Label(ramka_szczegoly_klienci, text="Lokalizacja:").grid(row=1, column=4, sticky=W)
label_det_klient_lok_val = Label(ramka_szczegoly_klienci, text="...")
label_det_klient_lok_val.grid(row=1, column=5, sticky=W, padx=10)
Label(ramka_szczegoly_klienci, text="Firma:").grid(row=1, column=6, sticky=W)
label_det_klient_firma_val = Label(ramka_szczegoly_klienci, text="...")
label_det_klient_firma_val.grid(row=1, column=7, sticky=W, padx=10)

# PRACOWNICY
# RAMKI
ramka_lista_prac = Frame(tab_pracownicy)
ramka_formularz_prac = Frame(tab_pracownicy)
ramka_szczegoly_prac = Frame(tab_pracownicy)

ramka_lista_prac.grid(row=0, column=0, padx=20, pady=10, sticky=N)
ramka_formularz_prac.grid(row=0, column=1, padx=20, pady=10, sticky=N)
ramka_szczegoly_prac.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky=W)

# Lista
Label(ramka_lista_prac, text="Lista pracowników:").grid(row=0, column=0, sticky=W)
listbox_pracownicy = Listbox(ramka_lista_prac, width=30)
listbox_pracownicy.grid(row=1, column=0, columnspan=3, pady=5)
Button(ramka_lista_prac, text="Szczegóły", command=show_employee_details).grid(row=2, column=0)
Button(ramka_lista_prac, text="Usuń", command=remove_employee).grid(row=2, column=1)
Button(ramka_lista_prac, text="Edytuj", command=edit_employee).grid(row=2, column=2)

# Formularz
Label(ramka_formularz_prac, text="Formularz:").grid(row=0, column=0, columnspan=2, sticky=W)
Label(ramka_formularz_prac, text="Imię:").grid(row=1, column=0, sticky=W)
Label(ramka_formularz_prac, text="Nazwisko:").grid(row=2, column=0, sticky=W)
Label(ramka_formularz_prac, text="Telefon:").grid(row=3, column=0, sticky=W)
Label(ramka_formularz_prac, text="Lokalizacja:").grid(row=4, column=0, sticky=W)
Label(ramka_formularz_prac, text="Firma:").grid(row=5, column=0, sticky=W)

entry_imie_pracownika = Entry(ramka_formularz_prac)
entry_nazwisko_pracownika = Entry(ramka_formularz_prac)
entry_telefon_pracownika = Entry(ramka_formularz_prac)
entry_lokalizacja_pracownika = Entry(ramka_formularz_prac)
combobox_firma_pracownika = ttk.Combobox(ramka_formularz_prac, state='readonly')

entry_imie_pracownika.grid(row=1, column=1)
entry_nazwisko_pracownika.grid(row=2, column=1)
entry_telefon_pracownika.grid(row=3, column=1)
entry_lokalizacja_pracownika.grid(row=4, column=1)
combobox_firma_pracownika.grid(row=5, column=1)

button_dodaj_pracownika = Button(ramka_formularz_prac, text="Dodaj pracownika", command=add_employee)
button_dodaj_pracownika.grid(row=6, column=0, columnspan=2, pady=10)

# Szczegóły
Label(ramka_szczegoly_prac, text="Szczegóły pracownika:").grid(row=0, column=0, sticky=W)
Label(ramka_szczegoly_prac, text="Imię:").grid(row=1, column=0, sticky=W)
label_det_prac_imie_val = Label(ramka_szczegoly_prac, text="...")
label_det_prac_imie_val.grid(row=1, column=1, sticky=W, padx=10)
Label(ramka_szczegoly_prac, text="Nazwisko:").grid(row=1, column=2, sticky=W)
label_det_prac_nazw_val = Label(ramka_szczegoly_prac, text="...")
label_det_prac_nazw_val.grid(row=1, column=3, sticky=W, padx=10)
Label(ramka_szczegoly_prac, text="Telefon:").grid(row=1, column=4, sticky=W)
label_det_prac_tel_val = Label(ramka_szczegoly_prac, text="...")
label_det_prac_tel_val.grid(row=1, column=5, sticky=W, padx=10)
Label(ramka_szczegoly_prac, text="Lokalizacja:").grid(row=2, column=0, sticky=W)
label_det_prac_lok_val = Label(ramka_szczegoly_prac, text="...")
label_det_prac_lok_val.grid(row=2, column=1, sticky=W, padx=10)
Label(ramka_szczegoly_prac, text="Firma:").grid(row=2, column=2, sticky=W)
label_det_prac_firma_val = Label(ramka_szczegoly_prac, text="...")
label_det_prac_firma_val.grid(row=2, column=3, sticky=W, padx=10)

# WARTOWNIE
# RAMKI
ramka_lista_wart = Frame(tab_wartownie)
ramka_formularz_wart = Frame(tab_wartownie)
ramka_szczegoly_wart = Frame(tab_wartownie)

ramka_lista_wart.grid(row=0, column=0, padx=20, pady=10, sticky=N)
ramka_formularz_wart.grid(row=0, column=1, padx=20, pady=10, sticky=N)
ramka_szczegoly_wart.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky=W)

# Lista
Label(ramka_lista_wart, text="Lista wartowni:").grid(row=0, column=0, sticky=W)
listbox_wartownie = Listbox(ramka_lista_wart, width=30)
listbox_wartownie.grid(row=1, column=0, columnspan=3, pady=5)
Button(ramka_lista_wart, text="Szczegóły", command=show_guardhouse_details).grid(row=2, column=0)
Button(ramka_lista_wart, text="Usuń", command=remove_guardhouse).grid(row=2, column=1)
Button(ramka_lista_wart, text="Edytuj", command=edit_guardhouse).grid(row=2, column=2)

# Formularz
Label(ramka_formularz_wart, text="Formularz:").grid(row=0, column=0, columnspan=2, sticky=W)
Label(ramka_formularz_wart, text="Nazwa:").grid(row=1, column=0, sticky=W)
Label(ramka_formularz_wart, text="Lokalizacja:").grid(row=2, column=0, sticky=W)
Label(ramka_formularz_wart, text="Firma:").grid(row=3, column=0, sticky=W)

entry_nazwa_wartowni = Entry(ramka_formularz_wart)
entry_lokalizacja_wartowni = Entry(ramka_formularz_wart)
combobox_firma_wartowni = ttk.Combobox(ramka_formularz_wart, state='readonly')

entry_nazwa_wartowni.grid(row=1, column=1)
entry_lokalizacja_wartowni.grid(row=2, column=1)
combobox_firma_wartowni.grid(row=3, column=1)

button_dodaj_wartownie = Button(ramka_formularz_wart, text="Dodaj wartownię", command=add_guardhouse)
button_dodaj_wartownie.grid(row=4, column=0, columnspan=2, pady=10)

# Szczegóły
Label(ramka_szczegoly_wart, text="Szczegóły wartowni:").grid(row=0, column=0, sticky=W)
Label(ramka_szczegoly_wart, text="Nazwa:").grid(row=1, column=0, sticky=W)
label_det_wart_nazwa_val = Label(ramka_szczegoly_wart, text="...")
label_det_wart_nazwa_val.grid(row=1, column=1, sticky=W, padx=10)
Label(ramka_szczegoly_wart, text="Lokalizacja:").grid(row=1, column=2, sticky=W)
label_det_wart_lok_val = Label(ramka_szczegoly_wart, text="...")
label_det_wart_lok_val.grid(row=1, column=3, sticky=W, padx=10)
Label(ramka_szczegoly_wart, text="Firma:").grid(row=1, column=4, sticky=W)
label_det_wart_firma_val = Label(ramka_szczegoly_wart, text="...")
label_det_wart_firma_val.grid(row=1, column=5, sticky=W, padx=10)

# FILTROWANIE MAPY - ZAKŁADKI
def filtruj_mape(event=None):
    for lista in [companies, clients, employees, guardhouses]:
        for obiekt in lista:
            if hasattr(obiekt, 'marker') and obiekt.marker is not None:
                try:
                    obiekt.marker.delete()
                except:
                    pass
                obiekt.marker = None
    wybrana_zakladka = notebook.tab(notebook.select(), "text")
    if wybrana_zakladka == "FIRMY":
        for f in companies:
            f.marker = map_widget.set_marker(f.coordinates[0], f.coordinates[1], text=f"Firma: {f.nazwa}")
    elif wybrana_zakladka == "KLIENCI":
        for k in clients:
            k.marker = map_widget.set_marker(k.coordinates[0], k.coordinates[1], text=f"Klient: {k.imie} {k.nazwisko}")
    elif wybrana_zakladka == "PRACOWNICY":
        for p in employees:
            p.marker = map_widget.set_marker(p.coordinates[0], p.coordinates[1],
                                             text=f"Pracownik: {p.imie} {p.nazwisko}")
    elif wybrana_zakladka == "WARTOWNIE":
        for w in guardhouses:
            w.marker = map_widget.set_marker(w.coordinates[0], w.coordinates[1], text=f"Wartownia: {w.nazwa}")



notebook.bind("<<NotebookTabChanged>>", filtruj_mape)
# START
show_companies()
show_clients()
show_employees()
show_guardhouses()
zaktualizuj_listy_wyboru()

filtruj_mape()
root.mainloop()