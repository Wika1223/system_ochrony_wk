from tkinter import *
from tkinter import ttk
import tkintermapview


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

root.mainloop()