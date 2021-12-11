import tkinter as tk
from time import strftime

my_w = tk.Tk()
my_w.geometry("405x170")



def get_time():
    time_string = strftime('%H:%M:%S %p')
    l1.config(text=time_string)
    l1.after(1000, get_time) 


my_font = ('times', 52, 'bold') 

l1 = tk.Label(my_w, font=my_font, bg='yellow')
l1.grid(row=1, column=1, padx=5, pady=25)

get_time()
