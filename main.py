from tkinter import *
from tkinter import ttk
import tkintermapview
from system_lib.model import Firma

#BAZA
companies = [
    Firma("Solid Security", "Warszawa", "521-03-21-528", "ul. Postępu 17"),
    Firma("Konsalnet", "Kraków", "527-20-27-282", "ul. Kamińskiego 1"),
    Firma("Securitas", "Poznań", "522-23-40-331", "ul. Dąbrowskiego 79A")]

def zaktualizuj_listy_wyboru():
    nazwy_firm = [f.nazwa for f in companies]


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


# FILTROWANIE MAPY - ZAKŁADKI
def filtruj_mape(event=None):
    for lista in [companies,]:
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

# START
show_companies()

root.mainloop()