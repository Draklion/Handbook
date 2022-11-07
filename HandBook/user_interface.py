import log
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import csv
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()  
root.title("Автопарк")
root.geometry("700x500+250+250")
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
                ID_conductor = buses_row['ID_conductor']
                log.Buses(f'Open and close file "Buses.csv", State_number:{buses_row["State_number"]}, ID_driver: {ID_driver}, ID_Maintenance: {ID_Maintenance}\n')
        
    with open("Drivers.csv",encoding="utf-8",newline="") as drivers_file:
        drivers_reader = csv.DictReader(drivers_file, delimiter=";")
        for drivers_row in drivers_reader:
            if ID_driver == drivers_row['ID_driver']:
                ST.insert(END, "Информация о водителе: ")
                ST.insert(END, f"{drivers_row['ID_driver'], drivers_row['Full_name'], drivers_row['Experience'], drivers_row['Open categories']}\n")
                log.Drivers(f'Open and close file "Drivers.csv", Full_name:{drivers_row["Full_name"]}, ID_driver: {ID_driver}\n')
                
    with open("Conductors.csv",encoding="utf-8",newline="") as сonductors_file:
        сonductors_reader = csv.DictReader(сonductors_file, delimiter=";")
        for сonductors_row in сonductors_reader:
            if ID_conductor == сonductors_row['ID_conductor']:
                ST.insert(END, "Информация о кондукторе: ")
                ST.insert(END, f"{сonductors_row['ID_conductor'], сonductors_row['Full_name'], сonductors_row['Work_experience']}\n")
                log.Drivers(f'Open and close file "Conductors.csv", Full_name:{сonductors_row["Full_name"]}, Work_experience: {сonductors_row}\n')
                
    with open("PTI.csv",encoding="utf-8",newline="") as pti_file:
        pti_reader = csv.DictReader(pti_file, delimiter=";")
        for pti_row in pti_reader:
            if ID_Maintenance == pti_row['ID_Maintenance']:
                ST.insert(END, "Информация о ТО: ")
                ST.insert(END, f"{pti_row['ID_Maintenance'], pti_row['Date_passage'], pti_row['ID_works']}\n")
                ID_works = pti_row['ID_works']
                log.PTI(f'Open and close file "PTI.csv", Date_passage:{pti_row["Date_passage"]}, ID_Maintenance: {ID_Maintenance}\n')

    with open("TTIW.csv",encoding="utf-8",newline="") as ttiw_file:
        ttiw_reader = csv.DictReader(ttiw_file, delimiter=";")
        for ttiw_row in ttiw_reader:
            if ID_works == ttiw_row['ID_works']:
                ST.insert(END, "Информация о видах работ ТО: ")
                ST.insert(END, f"{ttiw_row['ID_works'], ttiw_row['Types_work']}")
                log.PTI(f'Open and close file "TTIW.csv", ID_works:{ID_works}, Types_work: {ttiw_row["Types_work"]}\n')            
    return

tk.Button(root, text="Вывести результат", command=single_click, font=10,).pack(side=BOTTOM,pady=10)
tk.Label(root, text="Выбирите гос. номер автобуса:").place(x=20,y=0)
root.mainloop()