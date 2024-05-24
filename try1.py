# Authors: Artem Kii, Gaabriel Ponomarjov

# Imports
from customtkinter import *
import time

app = CTk()
app.title("Weather APP | Try1")
app.geometry("1000x600")
app.configure(bg='#1e1e1e')
app.resizable(width=False, height=False)

entry = CTkEntry(master=app, width=120, height=25, corner_radius=10, fg_color='#333333')
entry.place(relx=0.5, rely=0.1, anchor=CENTER)

app.mainloop()