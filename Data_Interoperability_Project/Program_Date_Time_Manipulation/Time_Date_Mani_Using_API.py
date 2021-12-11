from tkinter import *
import requests
import json
test =requests.get("http://worldtimeapi.org/api/timezone/")
tt=test.json()
top = Tk()
frame = Tk.frame(top)

top.geometry("550x230")
top.title("Date And Time Visualizer")
top.eval('tk::PlaceWindow . center')

menu = StringVar()
menu.set("Select the time Zone")

def getcurrent(selection):
   TimeDate_Data = requests.get("http://worldtimeapi.org/api/timezone/{0}".format(selection))
   data = TimeDate_Data.text
   test = 0
   parse_data=json.loads(data)
   label.config(text="Date - " + parse_data.get("datetime")[:10],bg="blue")
   label1.config(text="Time - " + parse_data.get("datetime")[11:19],bg="blue")


drop= OptionMenu(top, menu,*tt,command=getcurrent)
label = Label(top, fg="white", font=("Arial",52,'bold'))
label1 = Label(top, fg="white", font=("Arial",52,'bold'))
drop.pack(side="top")
label.pack()
label1.pack()
#Create a dropdown Menu
drop.config(width=90, font=('Helvetica', 12))


top.mainloop()
