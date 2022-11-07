import log
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import csv
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()  
root.title("Автопарк")
root.geometry("500x500+300+150")
cb = Combobox(root, values=("Нет","С568АО","В233АМ","С045РО","О002ОА"),justify=CENTER)
cb.current(0)
cb.pack()
ST = ScrolledText(root, wrap=WORD)
ST.pack()
ID_driver = ""

def single_click():
    ST.delete(1.0,END)
    
    with open("Buses.csv",encoding="utf-8",newline="") as buses_file:
        buses_reader = csv.DictReader(buses_file, delimiter=";")
        for buses_row in buses_reader:
            if cb.get() == buses_row['State_number']:
                    ST.insert(END, "Информация об автобусе: ")
                    ST.insert(END, f"{buses_row['Serial_number'], buses_row['State_number'], buses_row['ID_driver'], buses_row['ID_conductor'], buses_row['ID_Maintenance']}\n")
                    ID_driver = buses_row['ID_driver']
                    ID_Maintenance = buses_row['ID_Maintenance']
    
    with open("Drivers.csv",encoding="utf-8",newline="") as drivers_file:
        drivers_reader = csv.DictReader(drivers_file, delimiter=";")
        for drivers_row in drivers_reader:
            if ID_driver == drivers_row['ID_driver']:
                ST.insert(END, "Информация о водителе: ")
                ST.insert(END, f"{drivers_row['ID_driver'], drivers_row['Full_name'], drivers_row['Experience'], drivers_row['Open categories']}\n")
    
    with open("PTI.csv",encoding="utf-8",newline="") as pti_file:
        pti_reader = csv.DictReader(pti_file, delimiter=";")
        for pti_row in pti_reader:
            if ID_Maintenance == pti_row['ID_Maintenance']:
                ST.insert(END, "Информация о ТО: ")
                ST.insert(END, f"{pti_row['ID_Maintenance'], pti_row['Date_passage'], pti_row['ID_works']}")                
    return

tk.Button(root, text="Вывести результат", command=single_click, font=10,).place(x=150, y=450)

root.mainloop()