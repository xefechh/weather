# Authors: Artem Kii, Gaabriel Ponomarjov

# Imports
from customtkinter import *

app = CTk()
app.title("Weather APP")
app.geometry("500x400")

label = CTkLabel(master=app)
label.place(relx=0.5, rely=0.5, anchor='center')

app.mainloop()