import requests
from bs4 import BeautifulSoup
import re


def konwertuj_na_dziesietne(tekst: str) -> float:
    tekst = tekst.replace(',', '.')
    if '°' not in tekst:
        return float(tekst)
    liczby = re.findall(r"[\d\.]+", tekst)
    kierunek = tekst[-1].upper()
    stopnie = float(liczby[0]) if len(liczby) > 0 else 0
    minuty = float(liczby[1]) if len(liczby) > 1 else 0
    sekundy = float(liczby[2]) if len(liczby) > 2 else 0
    wynik = stopnie + (minuty / 60) + (sekundy / 3600)
    if kierunek in ['S', 'W']: wynik = -wynik
    return wynik


class Firma:
    def __init__(self, nazwa: str, lokalizacja: str, nip: str, adres: str):
        self.nazwa = nazwa
        self.lokalizacja = lokalizacja
        self.nip = nip
        self.adres = adres
        self.coordinates = self.get_coordinates()

    def get_coordinates(self) -> list:
        url = f'https://pl.wikipedia.org/wiki/{self.lokalizacja}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response_html = BeautifulSoup(response.text, features='html.parser')
        lat = response_html.select('.latitude')
        lon = response_html.select('.longitude')

        # --- ZABEZPIECZENIE (TO RATUJE KRAKÓW PRZED BŁĘDEM) ---
        if len(lat) > 0 and len(lon) > 0:
            return [konwertuj_na_dziesietne(lat[0].text), konwertuj_na_dziesietne(lon[0].text)]
        return None


class Klient:
    def __init__(self, imie: str, nazwisko: str, lokalizacja: str, przypisana_firma: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.lokalizacja = lokalizacja
        self.przypisana_firma = przypisana_firma
        self.coordinates = self.get_coordinates()

    def get_coordinates(self) -> list:
        url = f'https://pl.wikipedia.org/wiki/{self.lokalizacja}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response_html = BeautifulSoup(response.text, features='html.parser')
        lat = response_html.select('.latitude')
        lon = response_html.select('.longitude')
        if len(lat) > 0 and len(lon) > 0:
            return [konwertuj_na_dziesietne(lat[0].text), konwertuj_na_dziesietne(lon[0].text)]
        return None


class Pracownik:
    def __init__(self, imie: str, nazwisko: str, lokalizacja: str, przypisana_firma: str, telefon: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.lokalizacja = lokalizacja
        self.przypisana_firma = przypisana_firma
        self.telefon = telefon
        self.coordinates = self.get_coordinates()

    def get_coordinates(self) -> list:
        url = f'https://pl.wikipedia.org/wiki/{self.lokalizacja}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response_html = BeautifulSoup(response.text, features='html.parser')
        lat = response_html.select('.latitude')
        lon = response_html.select('.longitude')
        if len(lat) > 0 and len(lon) > 0:
            return [konwertuj_na_dziesietne(lat[0].text), konwertuj_na_dziesietne(lon[0].text)]
        return None


class Wartownia:
    def __init__(self, nazwa: str, lokalizacja: str, przypisana_firma: str):
        self.nazwa = nazwa
        self.lokalizacja = lokalizacja
        self.przypisana_firma = przypisana_firma
        self.coordinates = self.get_coordinates()

    def get_coordinates(self) -> list:
        url = f'https://pl.wikipedia.org/wiki/{self.lokalizacja}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response_html = BeautifulSoup(response.text, features='html.parser')
        lat = response_html.select('.latitude')
        lon = response_html.select('.longitude')
        if len(lat) > 0 and len(lon) > 0:
            return [konwertuj_na_dziesietne(lat[0].text), konwertuj_na_dziesietne(lon[0].text)]
        return None